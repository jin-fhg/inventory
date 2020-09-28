from django.contrib import admin
from .models import Profile, ItemFolder, Item, Tag

# Register your models here.
admin.site.register(Profile)
admin.site.register(ItemFolder)
admin.site.register(Item)
admin.site.register(Tag)


