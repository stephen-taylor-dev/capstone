from tokenize import group
from typing import Text
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, request
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.template.defaulttags import register
import random
import json
from .models import User, Liturgy, Group, Group_Invite, Comment, Prayer_Request

GROUP_ID = 0

def index(request):
    if request.user.is_authenticated:
        totalLiturgies = Liturgy.objects.count()
        userGroups = Group.objects.filter(members=request.user.id)
        
        # Always load a random liturgy on the first load up
        liturgy = get_object_or_404(Liturgy, pk=1)
        invites = Group_Invite.objects.filter(receiver=request.user, accepted=False)
        return render(request, "benedict_option/index.html", {
        "liturgy": liturgy,
        "totalLiturgies": totalLiturgies,
        "userGroups": userGroups,
        "invites": invites,
        })
    else:
        return HttpResponseRedirect(reverse("login"))

# Custom django filter to get dictionary key value
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def prayerRequests(request):
    if request.user.is_authenticated:
        userGroups = Group.objects.filter(members=request.user.id)
        comments = dict()
        prayer_requests = Prayer_Request.objects.filter(
                        group=request.user.active_group).order_by("-date_created").all()
        for item in prayer_requests:
            comments[item.id] = item.comments.order_by("-date_created").all()
        return render(request, "benedict_option/prayer-requests.html",{
            "prayer_requests": prayer_requests,
            "comments": comments,
            "userGroups": userGroups
        })
    else:
        return HttpResponseRedirect(reverse("login"))

@csrf_exempt
def searchLiturgy(request):
    query_dict = request.GET
    # Check to see if user searched for Title and Author or Phrase
    if query_dict.get('title-author') == None:
        search = Liturgy.objects.filter(text__contains=query_dict['phrase'])
    else:
        search = Liturgy.objects.filter(title__contains=query_dict['title-author']) | Liturgy.objects.filter(author__contains=query_dict['title-author'])
    print(search)
    num_results = search.count
    return render(request, "benedict_option/search.html", {
        "search_results": search,
        "num_results": num_results,
    })

def loadFeed(request):
    return render(request, "benedict_option/feed.html")


def loadLiturgy(request, id):
    count = Liturgy.objects.count()
    if id > count:
        return render(request, "benedict_option/index.html", {
                "message": "Item not found in database"
            })
    liturgy = get_object_or_404(Liturgy, pk=id)
    jsonLiturgy = liturgy.to_json()
    return JsonResponse(jsonLiturgy, safe=False)

def search(request):
    return render(request, "benedict_option/search.html",)


# refactor this - copied from index function
def pray(request):
    if request.user.is_authenticated:
        totalLiturgies = Liturgy.objects.count()
        userGroups = Group.objects.filter(members=request.user.id)
        
        # Always load a random liturgy on the first load up
        liturgy = get_object_or_404(Liturgy, pk=1)

        return render(request, "benedict_option/pray.html", {
        "liturgy": liturgy,
        "totalliturgies": totalLiturgies,
        "userGroups": userGroups,
        })
    else:
        return HttpResponseRedirect(reverse("login"))


@csrf_exempt
def createGroup(request):
    if request.method == "POST":
        # Check recipient invites
        user = get_object_or_404(User, pk=request.user.id)
        data = json.loads(request.body)
        newGroup = Group(name=data['group'])
        newGroup.save()
        newGroup.members.add(user)
        return JsonResponse({
           "message": "Created Group succesfully"}, status=201)

@csrf_exempt
def sendGroupInvites(request):
    # creating a new invite must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    # Check recipient invites
    data = json.loads(request.body)
    email_addresses = [email.strip() for email in data.get("recipients").split(",")]
    if email_addresses == [""]:
        return JsonResponse({
            "error": "At least one recipient required."
        }, status=400)

    # Convert email addresses to users
    recipients = []
    for address in email_addresses:
        try:
            user = User.objects.get(email=address)
            recipients.append(user)
        except User.DoesNotExist:
            return JsonResponse({
                "error": f"User with email {address} does not exist."
            }, status=400)

    # Get group name for invite
    group = data.get("group", '')
    group = Group.objects.get(id=group)


    # Create one invite for each recipient
    users = set()
    users.update(recipients)
    for user in users:
        invite = Group_Invite(

            sender=request.user,
            receiver=user,
            group=group,
        )
        invite.save()

    return JsonResponse({"message": "Invite sent successfully."}, status=201)


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
def createComment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = get_object_or_404(User, pk=request.user.id)
        prayer_request = get_object_or_404(Prayer_Request, pk=data["prayer_request"])
        comment = Comment(
                author=user,
                prayer_request=prayer_request,
                message=data["message"])
        comment.save()
        return JsonResponse({
           "message": "Comment created successfully."}, status=201)

@csrf_exempt
def createPRequest(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = get_object_or_404(User, pk=request.user.id)
        p_requst = Prayer_Request(
                creator=user,
                group=user.active_group,
                content=data["content"])
        p_requst.save()
        print(p_requst)
        return JsonResponse({
           "message": "Comment created successfully."}, status=201)

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
    return HttpResponseRedirect(reverse("login"))

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
            # Get public group
            group = Group.objects.get(pk=1)
            user = User.objects.create_user(username, email, password)
            user.active_group = group
            user.save()
        except IntegrityError:
            return render(request, "benedict_option/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "benedict_option/register.html")


@csrf_exempt
def respondToInvite(request):
    if request.method == "PUT":
        data = json.loads(request.body)
        group_invite = get_object_or_404(Group_Invite, id=data['invitation_id'])
        if data['delete'] == True:
             group_invite.delete()
        else:
            user = get_object_or_404(User, id=request.user.id)
            group = get_object_or_404(Group, id=data['group_id'])
            group_invite.accepted = True
            group_invite.save()
            group.members.add(user)
        return JsonResponse({
           "message": "Group invited updated"}, status=201)
