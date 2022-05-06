import uuid

from django.contrib.auth.models import User
from django.db import models
import datetime
import os


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)


class Item(models.Model):
    name = models.TextField(max_length=191)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)
    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'

    def __str__(self):
        return self.name



class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    category = models.ForeignKey(
    Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to=filepath, null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description