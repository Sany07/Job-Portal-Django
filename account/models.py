from django.contrib.auth.models import AbstractUser
from django.db import models

from account.managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    })
    gender = models.CharField(max_length=10, blank=True, null=True, default="")


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    objects = CustomUserManager()
