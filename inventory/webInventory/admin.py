from django.contrib import admin
from .models import Profile, ItemFolder, Item, Tag, UserRole, Role, companyInformation, UserCompany

# Register your models here.
admin.site.register(Profile)
admin.site.register(ItemFolder)
admin.site.register(Item)
admin.site.register(Tag)
admin.site.register(Role)
admin.site.register(UserRole)
admin.site.register(companyInformation)
admin.site.register(UserCompany)
