from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import logging
from django.contrib import messages
from .models import Profile, ItemFolder, Item, Tag, ItemTag, AuditTrail
from . import common
import json
# Create your views here.

logger = logging.getLogger(__name__)


def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['uname'], password=request.POST['pword'])
        if user is not None:
            login(request, user)
            if not 'remember' in request.POST:
                request.session.set_expiry(0)
            return redirect('home')
        else:
            messages.error(request, f'Login Failed. Incorrect Username or Password.')
            return redirect('login')
    return render(request, 'webInventory/login.html')

def logout_view(request):
    logout(request)
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['uname'], password=request.POST['pword'])
        if user is not None:
            login(request, user)
            if not 'remember' in request.POST:
                request.session.set_expiry(0)
            return redirect('home')
        else:
            messages.error(request, f'Login Failed. Incorrect Username or Password.')
            return redirect('login')
    else:
        messages.success(request, f'You are now logged out.')
        logout(request)
    return render(request, 'webInventory/login.html')


@login_required
def index(request):
    all_foldersCount = len(ItemFolder.objects.all())

    if request.method == 'POST':
        logger.error(request.POST)

    context = {
       'countFolder' : all_foldersCount,
       'countItemFolders' : common.countFolderItemsAll()
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
                newFolder.save()
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
        return redirect('itemList', pk)
    context = {
        'folder': folder,
        'itemList': itemList
    }

    return render(request, 'webInventory/itemList.html', context)


@login_required
def updateFolder(request):
    if request.method == 'POST':
        if request.is_ajax and request.user.is_authenticated:
            folder = ItemFolder.objects.get(id=request.POST['id'])
            whatToupdate = request.POST['update']
            if whatToupdate == 'name':
                if request.POST.get('value'):
                    folder.name = request.POST['value']
                    folder.save()
                    logger.error("Update Successful")
                    return HttpResponse("Update is Successful")
                else:
                    return HttpResponse("Update Not Successful")
            elif whatToupdate == 'description':
                folder.description = request.POST['value']
                folder.save()
                logger.error("Update Successful")
                return HttpResponse("Update is Successful")
    return HttpResponse(None)


@login_required
def loadChart(request, *args, **kwargs):
    data = common.AllFolderAndItems(2)
    return JsonResponse(data)
