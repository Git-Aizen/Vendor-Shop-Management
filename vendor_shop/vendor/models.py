from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models

class Vendor(AbstractUser):
    groups = models.ManyToManyField(Group, related_name="vendor_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="vendor_permissions", blank=True)

class Shop(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    business_type = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
