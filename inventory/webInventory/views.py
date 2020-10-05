from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import logging
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .models import Profile, ItemFolder, Item, Tag, ItemTag, AuditTrail
from . import common
from datetime import datetime
import json
# Create your views here.

logger = logging.getLogger(__name__)


def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['uname'], password=request.POST['pword'])
        if user is not None:
            login(request, user)
            AuditTrail.objects.create(action='Login', user_id = request.user.id, profile_name = request.user.profile.name)
            if not 'remember' in request.POST:
                request.session.set_expiry(0)
            return redirect('home')
        else:
            messages.error(request, f'Login Failed. Incorrect Username or Password.')
            return redirect('login')
    return render(request, 'webInventory/login.html')

def logout_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['uname'], password=request.POST['pword'])
        if user is not None:
            login(request, user)
            AuditTrail.objects.create(action='Login', user_id=request.user.id, profile_name=request.user.profile.name)
            if not 'remember' in request.POST:
                request.session.set_expiry(0)
            return redirect('home')
        else:
            messages.error(request, f'Login Failed. Incorrect Username or Password.')
            return redirect('login')
    else:
        AuditTrail.objects.create(action='Logout', user_id=request.user.id, profile_name=request.user.profile.name)
        messages.success(request, f'You are now logged out.')
        logout(request)
    return render(request, 'webInventory/login.html')


@login_required
def index(request):
    all_foldersCount = len(ItemFolder.objects.all())
    latest_audits = AuditTrail.objects.all().order_by('-created_on')[0:4]
    logger.error(latest_audits)
    if request.method == 'POST':
        logger.error(request.POST)

    context = {
       'countFolder' : all_foldersCount,
       'countItemFolders' : common.countFolderItemsAll(),
        'audits': latest_audits,
    }

    logger.error(common.AllFolderAndItems(2))

    return render(request, 'webInventory/index.html', context)


@login_required
def inventoryList(request):
    all_folders = ItemFolder.objects.all()

    #New Technique - Make the queryset a normal list so that you can update it
    folder_list = [{'id': x.id, 'name': x.name, 'description': x.description} for x in all_folders]

    #Add the number of items in the folder_list
    for folder in folder_list:
        all_itemsCount = len(Item.objects.filter(itemFolder_id=folder['id']))
        folder['itemCount'] = all_itemsCount

    if request.method == 'POST':
            if 'btnSave' in request.POST:
                newFolder = ItemFolder.objects.create(name=request.POST['newFolder'],
                                                      description=request.POST['folderDescription'],
                                                      created_by_id= request.user.id,
                                                      created_by_name= request.user.profile.name)

                AuditTrail.objects.create(action='Added', what='Item Storage:' + newFolder.name,
                                          profile_name=request.user.profile.name,
                                          user_id = request.user.id)

                messages.success(request, f'Folder Added Successfully')
                return redirect('inventoryList')
            elif 'saveDeleteOption' in request.POST:
                folder = ItemFolder.objects.get(id = request.POST['deleteOptionId'])

                AuditTrail.objects.create(action='Deleted', what='Item Storage:' + folder.name,
                                          profile_name=request.user.profile.name,
                                          user_id=request.user.id)
                folder.delete()
                messages.success(request, f'Folder Deleted Successfully')
                return redirect('inventoryList')
            else:
                logger.error("No POST")
    context = {
        'folders' : folder_list,
    }

    return render(request, 'webInventory/inventoryList.html', context)


@login_required
def itemList(request, pk):
    folder = ItemFolder.objects.get(id=pk)
    itemList = Item.objects.filter(itemFolder_id=pk)

    if request.method == 'POST':
        item = Item.objects.create(itemFolder_id = pk, name = request.POST['name'], price = request.POST['price'],
                                   quantity = request.POST['quantity'], minQuantity= request.POST['min-quantity'],
                                   description = request.POST['description'])
        AuditTrail.objects.create(action='Added', what=item.name + ' to Folder ' + folder.name,
                                  profile_name=request.user.profile.name,
                                  user_id=request.user.id)
        messages.success(request, f'Item Added Successfully')
        return redirect('itemList', pk)

    #ean = common.create_barcode(1)
    #logger.error(ean)
    context = {
        'folder': folder,
        'itemList': itemList
    }

    return render(request, 'webInventory/itemList.html', context)

def tagList(request):
    tags = Tag.objects.all()
    if request.method == 'POST':
        if 'addTag' in request.POST:
            tag_name = request.POST['tagName']
            if tag_name:
                newTag = Tag.objects.create(name=tag_name, created_by_id=request.user.id,
                                   created_by_name=request.user.profile.name)

                AuditTrail.objects.create(action='Added', what='Tag:' + newTag.name,
                                          profile_name=request.user.profile.name,
                                          user_id=request.user.id)

                messages.success(request, f'Item Added Successfully')
                return redirect('tagList')
        elif 'deleteOptionId' and 'saveDeleteOption' in request.POST:
            tag = Tag.objects.get(id=request.POST['deleteOptionId'])

            AuditTrail.objects.create(action='Deleted', what='Tag:' + tag.name,
                                      profile_name=request.user.profile.name,
                                      user_id=request.user.id)

            tag.delete()
            messages.success(request, f'Tag has been Deleted')
            return redirect('tagList')

    context = {
        'tags': tags,
    }
    return render(request, 'webInventory/tagList.html', context)

@login_required
def manageUsers(request):
    users = User.objects.all()
    profiles_temp = []
    profiles = []
    for user in users:
        profiles_temp.append(user.id)
        profiles_temp.append(user.username)
        profiles_temp.append(Profile.objects.get(user_id=user.id).name)
        profiles_temp.append(Profile.objects.get(user_id=user.id).created_on)
        profiles.append(profiles_temp)
        profiles_temp = []

    logger.error(profiles)
    context = {
        'users': profiles,
    }
    return render(request, 'webInventory/manageUsers.html', context)


@login_required
def auditTrail(request):
    if request.method == 'POST':
        audits = AuditTrail.objects.filter(created_on__range=[str(request.POST['dateFrom']) + ' 00:00:00',
                                                              str(request.POST['dateTo']) + ' 23:59:59']).order_by('-id')
        logger.error(audits)
    else:
        audits = AuditTrail.objects.all().order_by('-id')

    context = {
        'audits': audits
    }
    return render(request, 'webInventory/auditTrail.html', context)

#Ajaxes
@login_required
def updateFolder(request):
    if request.method == 'POST':
        if request.is_ajax and request.user.is_authenticated:
            folder = ItemFolder.objects.get(id=request.POST['id'])
            whatToupdate = request.POST['update']
            if whatToupdate == 'name':
                if request.POST.get('value'):
                    folder_from = folder.name
                    folder.name = request.POST['value']

                    AuditTrail.objects.create(action='Updated', what= 'Folder Name',
                                              action_from = folder_from,
                                              action_to = folder.name,
                                              profile_name=request.user.profile.name,
                                              user_id=request.user.id)

                    folder.save()
                    logger.error("Update Successful")
                    return HttpResponse("Update is Successful")
                else:
                    return HttpResponse("Update Not Successful")
            elif whatToupdate == 'description':
                folder_from = folder.description
                folder.description = request.POST['value']

                AuditTrail.objects.create(action='Updated', what='Folder Description ',
                                          action_from=folder_from,
                                          action_to = folder.description,
                                          profile_name=request.user.profile.name,
                                          user_id=request.user.id)

                folder.save()
                logger.error("Update Successful")
                return HttpResponse("Update is Successful")
    return HttpResponse(None)


@login_required
def updateTagName(request):
    if request.method == 'POST' and request.is_ajax:
       if request.POST['update'] == 'tagNameUpdate' and request.POST['value']:
            tag = Tag.objects.get(id = request.POST['id'])
            tag_from = tag.name
            tag.name = request.POST['value']

            AuditTrail.objects.create(action='Updated', what='Tag Name ',
                                      action_from=tag_from,
                                      action_to= tag.name,
                                      profile_name=request.user.profile.name,
                                      user_id=request.user.id)

            tag.save()
            logger.error("Success")
            return HttpResponse("Success")
    return HttpResponse(None)


@login_required
def loadChart(request, *args, **kwargs):
    data = common.AllFolderAndItems(2)
    return JsonResponse(data)
