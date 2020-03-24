from django.contrib import admin
from . import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'created', 'updated']
    list_filter = ['created', 'updated']
    list_editable = ['price', 'stock']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.User)
admin.site.register(models.Purchase)


