from django.contrib import admin
from .models import signup,login
# Register your models here.

class signup_admin(admin.ModelAdmin):
    list_display = ['Name','Email','Password']
admin.site.register(signup,signup_admin)

class login_admin(admin.ModelAdmin):
    list_display = ['Email','Password']

admin.site.register(login,login_admin)