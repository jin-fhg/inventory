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


def getCompanyOptions():
    options = ['EAN8', 'EAN13', 'EAN14']
    #barcode to be supported in the future 'UPCA', 'JAN', 'ISBN10', 'ISBN13', 'ISSN', 'Code39', 'Code128', 'PZN'
    return options


#Ipagpaliban na muna
#Generate barcode using Item tag and ITem ID. Format is EAN13
def create_barcode(item, request):
    country_code = 63
    companyDetails = getCompany(request)
    country_code_length = len(str(country_code))

    #Check what barcode Type is in the selection to Identify the length
    if str.upper(companyDetails.barcodeType) == 'EAN8':
        barlength = 8
    elif str.upper(companyDetails.barcodeType) == 'EAN13':
        barlength = 13
    elif str.upper(companyDetails.barcodeType) == 'EAN14':
        barlength = 14

    #If Company Prefix is Not Null
    if companyDetails.companyPrefix:
        #Get the length of the Prefix
        companyPrefix_length = len(str(companyDetails.companyPrefix))
        # Shorten the String for universal usage
        companyPrefix = companyDetails.companyPrefix

    #If  Company Prefix is NULL
    else:
        #Creates a Company Prefix Default that looks like 0000
        companyPrefixDefault = ''
        if str.upper(companyDetails.barcodeType) == 'EAN13':
            companyPrefix_length = int((barlength - 3) / 2)
        else:
            companyPrefix_length = (barlength - 2) / 2
            companyPrefix_length = int(companyPrefix_length)

        for i in range(companyPrefix_length):
            companyPrefixDefault = companyPrefixDefault + '0'
        # Shorten the String for universal usage
        companyPrefix = companyPrefixDefault

    #Get the Product Code Length based on the length of the Company Prefix and Country code and barlength
    productCode_length = barlength - (companyPrefix_length + country_code_length)

    if str.upper(companyDetails.barcodeType) == 'EAN13':
        productCode_length = productCode_length-1

    #Deduct the item id length from the product code length
    productCode_length = productCode_length - len(str(item.id))

    #Product Code String always starts with 1
    productCode_string = '1'

    if productCode_length > 0:
        for x in range(productCode_length - 1):
            productCode_string = productCode_string + '0'

        productCode_string = productCode_string + str(item.id)

        # print(productCode_string)
        item_barcode = str(country_code) + companyPrefix + productCode_string
        #ean = barcode.get(companyDetails.barcodeType,
                          #str(country_code) + companyPrefix + productCode_string,
                          #writer=ImageWriter())
    elif productCode_length == 0:
        item_barcode = str(country_code) + companyPrefix + str(item.id)

    else:
        default = ''
        for x in range(barlength):
            default = default + '0'

        item_barcode = default

        #ean = barcode.get(companyDetails.barcodeType,
                          #default,
                          #writer=ImageWriter())

    #filename = ean.save('media/ean13')

    if str.upper(companyDetails.barcodeType) == 'EAN13':
       item_barcode = '0' + item_barcode

    return item_barcode


def generate_barcode(item, request):
    companyDetails = getCompany(request)
    ean = barcode.get(companyDetails.barcodeType, item.barcode, writer=ImageWriter())
    filename = ean.save('media/ean13')
    return filename

def getCompany(request):
    companyDesignation = UserCompany.objects.filter(user_id=request.user.id).order_by('-assigned_date')[0]
    companyDetails = companyInformation.objects.get(id=companyDesignation.company_id)
    return companyDetails

def Convert(string):
    # Use split to the string to return the data as an array and to capture the desired string
    li = string.split(":")  #split the String into an array using the : char on the string
    convertedData = []
    for item in range(1, len(li)):
        str = li[item].split('"')  #split again starting from the second element, this time, it uses the " character in the string of the element
        convertedData.append(str[1])
        #print(str[1], "Print from Function") #print the 1st element and return it
    return convertedData