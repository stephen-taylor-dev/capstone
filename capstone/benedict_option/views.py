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
from .models import User, Liturgy, Group


def index(request):
    totalLiturgies = Liturgy.objects.count()
    userGroups = Group.objects.filter(members=request.user.id)
    
    # Always load a random liturgy on the first load up
    liturgy = get_object_or_404(Liturgy, pk=random.randint(1, totalLiturgies))

    return render(request, "benedict_option/index.html", {
    "liturgy": liturgy,
    "totalLiturgies": totalLiturgies,
    "userGroups": userGroups,
    })

def loadFeed(request):
    return render(request, "benedict_option/feed.html")

def loadLiturgyLength(request, length):
    liturgies = Liturgy.objects.filter(length=length)
    liturgy_count = liturgies.count()
    random_index = 0
    if liturgy_count >= 1:
        random_index = random.randint(0, liturgy_count-1)
    liturgy = liturgies[random_index]
    jsonLiturgy = liturgy.to_json()
    return JsonResponse(jsonLiturgy, safe=False)

def loadLiturgy(request, id):
    count = Liturgy.objects.count()
    if id > count:
        return render(request, "benedict_option/index.html", {
                "message": "Item not found in database"
            })
    liturgy = get_object_or_404(Liturgy, pk=id)
    jsonLiturgy = liturgy.to_json()
    return JsonResponse(jsonLiturgy, safe=False)

# refactor this - copied from index function
def pray(request):
    totalLiturgies = Liturgy.objects.count()
    userGroups = Group.objects.filter(members=request.user.id)
    
    # Always load a random liturgy on the first load up
    liturgy = get_object_or_404(Liturgy, pk=random.randint(1, totalLiturgies))

    return render(request, "benedict_option/pray.html", {
    "liturgy": liturgy,
    "totalliturgies": totalLiturgies,
    "userGroups": userGroups,
    })



@csrf_exempt
def favoriteLiturgy(request):
    if request.method == "POST":
        user = User.objects.get(pk=request.user.id)
        data = json.loads(request.body)
        liturgyID = data["liturgy"]
        user.favorite_liturgies.add(int(liturgyID))
        user.save()
        return JsonResponse({
           "message": "Post edited successfully."}, status=201)

@csrf_exempt
def switchGroups(request):
    if request.method == "POST":
        user = User.objects.get(pk=request.user.id)
        data = json.loads(request.body)
        groupID = data["group"]
        newGroup = get_object_or_404(Group, pk=groupID)
        user.active_group = newGroup
        user.save()
        jsonGroup = newGroup.to_json()
        return JsonResponse({
           "group": jsonGroup,
           "message": "Switched groups successfully."
           }, safe=False, status=201)



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
