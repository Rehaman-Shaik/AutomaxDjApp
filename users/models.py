from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Location(models.Model):
    address1 = models.CharField(max_length=124)
    address2 = models.CharField(max_length=124, null=True, blank=True)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=40)
    zipcode=models.CharField(max_length=8)
    
    def __str__(self):
        return f'Location{self.id}'
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True)     
    bio = models.CharField(max_length=150, null=True, blank=True)
    phone_number =models.CharField(max_length=12, null=True, blank=True)
    location=models.OneToOneField(Location, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.user.username}\'s Profile"