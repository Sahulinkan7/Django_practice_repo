from django.db import models

from django.contrib.auth.models import User 


# Create your models here.
class Song(models.Model):
    user=models.ManyToManyField(User)
    song_duration=models.DecimalField(max_digits=4,decimal_places=2)
    song_name=models.CharField(max_length=100)
    
    def written_by(self):
        return ",".join([str(u) for u in self.user.all()])