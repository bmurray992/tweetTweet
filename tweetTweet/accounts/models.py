from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Profile(AbstractUser):
    username = models.CharField(("username"), max_length=50, unique=True)
    email = models.EmailField(("email address"), unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True)

    USERNAME_FIELD = 'username'
    def __str__(self):
        return "@" + self.username