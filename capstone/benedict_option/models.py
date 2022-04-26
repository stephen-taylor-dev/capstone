from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass

class TextModel(models.Model):
    author = models.TextField()
    text = models.TextField()
    title = models.TextField()


