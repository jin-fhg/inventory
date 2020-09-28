from .models import *

#This is for the most common Functions

#This count the item per folder individually
def countFolderItems(id):
    folder = ItemFolder.objects.get(id=id)
    itemCount = len(models.Item.objects.filter(itemFolder_id=folder.id))
    return itemCount

#This returns the total items of all folders
def countFolderItemsAll():
    all_folders = ItemFolder.objects.all()
    folder_list = [{'id': x.id} for x in all_folders]
    itemCount = 0
    for folder in folder_list:
        itemCount += len(Item.objects.filter(itemFolder_id=folder['id']))

    return itemCount


#This returns the name, id, and item quantity
def AllFolderAndItems(option):
    all_folders = ItemFolder.objects.all()

    if option == 1:
        folder_list = [{'id': x.id, 'name': x.name} for x in all_folders]
        for folder in folder_list:
            itemCount = len((Item.objects.filter(itemFolder_id=folder['id'])))
            folder['countItems'] = itemCount
            folder['barColor'] = '#2DAF36'
            folder['borderColor'] = '#3AB037'
    elif option == 2:
        folder_id = []
        folder_names = []
        itemCountList = []
        barColor = []
        borderColor = []
        for x in all_folders:
            itemCount = len((Item.objects.filter(itemFolder_id=x.id)))
            folder_id.append(x.id)
            folder_names.append(x.name)
            itemCountList.append(itemCount)
            barColor.append('#2DAF36')
            borderColor.append('#2DAF36')

        folder_list = {
            'ids' : folder_id,
            'names': folder_names,
            'itemCountList': itemCountList,
            'barColors': barColor,
            'borderColors': borderColor
        }

    return folder_list
