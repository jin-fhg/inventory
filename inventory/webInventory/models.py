from django.db import models
from django.contrib.auth.models import User, Group
from datetime import datetime, timedelta

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null= True)
    emp_id = models.CharField(max_length=100, blank=True, null= True)
    email = models.CharField(max_length=50, blank=True, null= True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    alt_phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.now, null=True, blank=True)

    def __str__(self):
        return self.name

class ItemFolder(models.Model):
    name = models.CharField(max_length=30, blank=True, null= True)
    barcode = models.BigIntegerField(null=True, blank=True, default=0)
    description = models.CharField(max_length=500, null=True, blank=True)
    created_on = models.DateTimeField(default=datetime.now)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_by_name = models.CharField(max_length=100, blank=True, null= True)
    def __str__(self):
        return self.name

class Item(models.Model):
    itemFolder = models.ForeignKey(ItemFolder, on_delete=models.CASCADE, null= True, blank=True)
    name = models.CharField(max_length=60, null=True, blank=True)
    sku = models.CharField(max_length=7, null=True, blank=True)
    barcode = models.BigIntegerField(null=True, blank=True, default=0)
    description = models.CharField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits= 12, decimal_places= 2, null=True, blank= True)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    minQuantity = models.IntegerField(null=True, blank=True, default=0)
    created_on = models.DateTimeField(default=datetime.now)
    last_update = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, blank=True, null= True)
    created_on = models.DateTimeField(default=datetime.now)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    created_by_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name



class ItemTag(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null= True, blank= True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null= True, blank= True)


class AuditTrail(models.Model):
    action = models.CharField(max_length=50, blank=True, null= True)
    what = models.CharField(max_length=100, blank=True, null= True)
    how_many = models.CharField(max_length=100, blank=True, null= True)
    action_from = models.CharField(max_length=100, blank=True, null=True)
    action_to = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    profile_name = models.CharField(max_length=100, null= True, blank=True)
    created_on = models.DateTimeField(default=datetime.now)


class Role(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.username + ' ' + self.role.name