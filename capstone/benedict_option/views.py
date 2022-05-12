from typing import Text
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, request
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import random
import json
from .models import User, Prayer, Group


def index(request):
    totalPrayers = Prayer.objects.count()
    userGroups = Group.objects.filter(members=request.user.id)
    
    # Always load a random prayer on the first load up
    prayer = get_object_or_404(Prayer, pk=random.randint(1, totalPrayers))

    return render(request, "benedict_option/index.html", {
    "prayer": prayer,
    "totalPrayers": totalPrayers,
    "userGroups": userGroups,
    })

def loadFeed(request):
    return render(request, "benedict_option/feed.html")

def loadPrayerLength(request, length):
    prayers = Prayer.objects.filter(length=length)
    prayer_count = prayers.count()
    random_index = 0
    if prayer_count >= 1:
        random_index = random.randint(0, prayer_count-1)
    prayer = prayers[random_index]
    jsonPrayer = prayer.to_json()
    return JsonResponse(jsonPrayer, safe=False)

def loadPrayer(request, id):
    count = Prayer.objects.count()
    if id > count:
        return render(request, "benedict_option/index.html", {
                "message": "Item not found in database"
            })
    prayer = get_object_or_404(Prayer, pk=id)
    jsonPrayer = prayer.to_json()
    return JsonResponse(jsonPrayer, safe=False)

def pray(request):
    return render(request, "benedict_option/pray.html")


@csrf_exempt
def favoritePrayer(request):
    if request.method == "POST":
        user = User.objects.get(pk=request.user.id)
        data = json.loads(request.body)
        prayerID = data["prayer"]
        user.favorite_prayers.add(int(prayerID))
        user.save()
        return JsonResponse({
           "message": "Post edited successfully."}, status=201)

def unfollow(request):
    if request.method == "POST":
        user = User.objects.get(pk=request.user.id)
        # Removes the user's profile to authenticated user's following list
        user.following.remove(int(request.POST["user_profile"]))
        return HttpResponseRedirect(reverse("index"))


# Copied from CS33a Project 4. Modified url paths
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "benedict_option/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "benedict_option/login.html")


# Copied from CS33a Project 4. Modified url paths
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# Copied from CS33a Project 4. Modified url paths
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "benedict_option/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "benedict_option/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "benedict_option/register.html")
