from django.contrib import admin
from .models import Products, Photo, Category

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Photo)