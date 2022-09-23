from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

# Create your models here.

class User(AbstractUser):

    # Many to many relationship for Users to track their favorite liturgies
    favorite_liturgies = models.ManyToManyField("Liturgy", blank=True, related_name="favorite_liturgies")
    uploaded_liturgies = models.ManyToManyField("Liturgy", blank=True, related_name="uploaded_liturgies")
    viewed_liturgies = models.ManyToManyField("Liturgy", blank=True, related_name="viewed_liturgies")
    # Everyone part of default public group
    active_group = models.ForeignKey("Group", blank=True, null=True, on_delete=models.CASCADE, related_name="active_group")


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
    members = models.ManyToManyField("User", blank=True, related_name="group_members")
    unique_name = models.UUIDField(default=uuid.uuid4, editable=False)
    group_admin = models.ForeignKey("User", blank=True, null=True, on_delete=models.CASCADE, related_name="admin")
    current_prayer = models.ForeignKey("Liturgy", blank=True, null=True, on_delete=models.CASCADE, related_name="current_prayer")
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
        }

    def __str__(self):
        return f"{self.name}"

# Allows users to be invited to join groups
class Group_Invite(models.Model):
    sender = models.ForeignKey("User", blank=True, null=True, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey("User", blank=True, null=True, on_delete=models.CASCADE, related_name="receiver")
    group = models.ForeignKey("Group", blank=True, null=True, on_delete=models.CASCADE, related_name="group")
    timestamp = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f"{self.sender} invited {self.receiver } to group - {self.group}"


class Prayer_Request(models.Model):
    creator= models.ForeignKey("User", on_delete=models.CASCADE, related_name="creator")
    group = models.ForeignKey("Group", blank=True, null=True, on_delete=models.CASCADE, related_name="request_group")
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.creator} in {self.group}"


class Comment(models.Model):
    author = models.ForeignKey("User", on_delete=models.CASCADE, related_name="commentor")
    prayer_request = models.ForeignKey("Prayer_Request",  on_delete=models.CASCADE, related_name="comments")
    date_created = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    def __str__(self):
        return f"{self.author} on Prayer Request {self.prayer_request.id}"