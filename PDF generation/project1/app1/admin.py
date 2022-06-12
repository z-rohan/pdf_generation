from django.contrib import admin
from .models import Laptop

# Register your models here.
class LaptopAdmin(admin.ModelAdmin):
    list_display=['lid','name','brand','ram','rom','hdd','ssd','price']

admin.site.register(Laptop,LaptopAdmin)