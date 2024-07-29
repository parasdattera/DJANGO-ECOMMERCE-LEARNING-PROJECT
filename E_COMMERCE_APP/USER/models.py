from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.email
    ...

    


