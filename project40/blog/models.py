from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Post(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    post_title=models.CharField(max_length=100)
    post_desc=models.CharField(max_length=4000)
    post_publish_date=models.DateField()
    
