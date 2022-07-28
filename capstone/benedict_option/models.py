from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    # Many to many relationship for Users to track their favorite liturgies
    favorite_liturgies = models.ManyToManyField("Liturgy", related_name="favorite_liturgies")
    uploaded_liturgies = models.ManyToManyField("Liturgy", related_name="uploaded_liturgies")
    viewed_liturgies = models.ManyToManyField("Liturgy", related_name="viewed_liturgies")
    current_group = models.ForeignKey("Group", blank=True, null=True, on_delete=models.CASCADE, related_name="current_group")
   

class Liturgy(models.Model):
    # fixes plural display in admin console
    class Meta:
        verbose_name_plural = "liturgies"
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


