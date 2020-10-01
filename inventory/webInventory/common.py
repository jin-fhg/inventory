from .models import *
import barcode
from barcode.writer import ImageWriter

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
            folder['borderColor'] = '#285E70'
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
            borderColor.append('#285E70')

        folder_list = {
            'ids' : folder_id,
            'names': folder_names,
            'itemCountList': itemCountList,
            'barColors': barColor,
            'borderColors': borderColor
        }

    return folder_list


#Ipagpaliban na muna
#Generate barcode using Item tag and ITem ID. Format is EAN13
def create_barcode(itemID):
    ean13 = ''
    manufacturer_number = ''
    item = Item.objects.get(id=itemID)
    barcode = manufacturer_number+item.sku
    ean = barcode.get('ean13', barcode , writer=ImageWriter())
    filename = ean.save('ean13')

    return filename

