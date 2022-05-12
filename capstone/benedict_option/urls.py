from  django.urls import path  
from . import views  

urlpatterns = [      
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("pray", views.pray, name="pray"),
    path("feed", views.loadFeed, name="feed"),

    # API Paths
    path("prayer/<int:length>", views.loadPrayerLength, name="loadPrayerLength"),
    path("prayer-navigate/<int:id>", views.loadPrayer, name="loadPrayer"),
    path("prayer-favorite", views.favoritePrayer, name="favoritePrayer"),
    

]