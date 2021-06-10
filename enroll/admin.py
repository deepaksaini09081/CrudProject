from django.contrib import admin
from .models import User,User2
# Register your models here.
########################################################################################################################
# @admin.register(User2)
# class UserAdmin1(admin.ModelAdmin):  
#     list_display=('id','name','email','sub','password','add')  
########################################################################################################################
class UserAdmin1(admin.ModelAdmin):
    list_display=['id','name','email','sub','password','add']
admin.site.register(User2,UserAdmin1)   
###################################################################################################################### 
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')
