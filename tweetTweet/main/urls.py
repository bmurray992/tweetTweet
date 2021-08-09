from django.urls import path 
from . import views 

urlpatterns = [
    path("@<str:username>/", views.Timeline.as_view(), name="timeline"),
    path("c/<int:tweet_id>/", views.conversation, name="conversation"),
    path('', views.Home.as_view(), name="home"),
]
