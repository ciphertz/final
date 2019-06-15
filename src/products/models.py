# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.urls import reverse
from django.core.files.storage import FileSystemStorage

from django.db import models


protected_loc = settings.MEDIA_ROOT

def download_loc(instance,filename):
    return "%s/%s" %(instance.slug, filename)
    # if instance.user.username:
    #     return "%s/download/%s" %(instance.user.username,filename)
    # else:
    #     return "%s/download/%s" %("default",filename)


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=500,null=True,blank=True)
    download = models.FileField(upload_to=download_loc,storage=FileSystemStorage(location=protected_loc),null=True,blank=True)
    price = models.DecimalField(max_digits=60,decimal_places=2)
    sale_price = models.DecimalField(max_digits=60,decimal_places=2,null=True,blank=True)
    slug= models.SlugField()

    def __str__(self):
        return self.name
