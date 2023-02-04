from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.base_user import BaseUserManager
    
from .managers import CustomUserManager

# Create your models here.
class MyUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [email, first_name, last_name, phone]

    objects = CustomUserManager()
    backend = 'teamlist.backend.CustomBackend'

    def __str__(self):
        return self.email


