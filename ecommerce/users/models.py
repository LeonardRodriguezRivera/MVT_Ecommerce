from django.db import models


class User_profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='profile_image/', blank=True)
    city = models.CharField(max_length=60, blank=True)

def __str__(self):
    return self.user.username + ' - profile'