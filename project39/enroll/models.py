from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # user=models.OneToOneField(User,on_delete=models.CASCADE,limit_choices_to={'is_staff':True})
    address=models.CharField(max_length=1000)
    adharid=models.CharField(max_length=12)
    
    def __str__(self):
        return self.adharid