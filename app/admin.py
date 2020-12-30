from django.contrib import admin
from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    
    list_display = ("id", "user","text","image", "date_created")
    list_editable = ("user", "text","image")

class ProfileAdmin(admin.ModelAdmin):
    
    list_display = ("id", "user","image","bio")
    list_editable = ("user","image","bio")




admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)