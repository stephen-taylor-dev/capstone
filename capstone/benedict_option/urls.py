from django.urls import path  
from . import views  

urlpatterns = [      
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("pray", views.pray, name="pray"),
    path("feed", views.loadFeed, name="feed"),

    # API Paths
    path("liturgy/<int:length>", views.loadLiturgyLength, name="loadLiturgyLength"),
    path("liturgy-navigate/<int:id>", views.loadLiturgy, name="loadLiturgy"),
    path("liturgy-favorite", views.favoriteLiturgy, name="favoriteLiturgy"),
    path("switch-groups", views.switchGroups, name="switchGroups"),
    

]