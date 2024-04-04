from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='avatars/', default='default.jpg',blank=True, null=True)
    bio = models.CharField(max_length=255, null = True, blank = True)
    location = models.CharField(max_length=255, null=True, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username

# create a user profile by default whennew user registers

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

#  automate the creation of a user profile

post_save.connect(create_profile, sender=User)