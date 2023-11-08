from django.contrib import admin

# Register your models here.
from .models import UserProfile

@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','user','address','adharid']
    list_display_links=['id','user']