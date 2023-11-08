from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display=['id','user','post_title','post_desc','post_publish_date']
