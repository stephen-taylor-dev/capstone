from django.urls import path  
from . import views  

urlpatterns = [      
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("pray", views.pray, name="pray"),
    path("search", views.search, name="search"),
    path("prayer-request", views.prayerRequests, name="prayer_requests"),

    # API Paths
    path("liturgy-navigate/<int:id>", views.loadLiturgy, name="loadLiturgy"),
    path("liturgy-favorite", views.favoriteLiturgy, name="favoriteLiturgy"),
    path("switch-groups", views.switchGroups, name="switchGroups"),
    path("send-invite", views.sendGroupInvites, name="sendGroupInvites"),
    path("create-group", views.createGroup, name="createGroup"),
    path("create-comment", views.createComment, name="createComment"),
    path("create-prequest", views.createPRequest, name="createPRequest"),
    path("search-liturgy", views.searchLiturgy, name="searchLiturgy"),
    path("respond-invite", views.respondToInvite, name="respondToInvite")
    
    
    

]