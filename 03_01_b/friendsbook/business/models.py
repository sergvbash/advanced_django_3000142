from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.
class Business(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=CASCADE)
    name = models.CharField(max_length=140)
    founded = models.DateField()
    location = models.CharField(max_length=200)
    created_on = models.DateTimeField('date created', auto_now_add=True)
    about = models.TextField(null=True)
    profile_photo = models.ImageField(upload_to='profile_photos', null=True)
    
    def __str__(self):
        return self.name[0:100]

    @property
    def birthday(self):
        return self.founded