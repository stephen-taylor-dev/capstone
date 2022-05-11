from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    # Many to many relationship for Users to track their favorite prayers
    favorite_prayers = models.ManyToManyField("Prayer", related_name="favorite_prayers")
    uploaded_prayers = models.ManyToManyField("Prayer", related_name="uploaded_prayers")
    viewed_prayers = models.ManyToManyField("Prayer", related_name="viewed_prayers")
    current_group = models.ForeignKey("Group", on_delete=models.CASCADE, related_name="current_group")
   

class Prayer(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    length = models.IntegerField()

    def to_json(self):
        return {
            "id": self.id,
            "author": self.author,
            "text": self.text,
            "title": self.title,
            "type": self.type,
            "length": self.length,
        }

    def __str__(self):
        return f"{self.title} - {self.author} - {self.type}"

class Group(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField("User", related_name="group_members")

    def __str__(self):
        return f"{self.name}"


