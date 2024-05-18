from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    """Модель пользователя. Предназначена для совместного использования членами компании"""
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
