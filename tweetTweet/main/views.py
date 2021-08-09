from django import http
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from accounts.models import Profile
from .models import Tweet
from django.views.generic import DetailView, ListView

# Create your views here.
class Home(ListView):
    model = Tweet
    template_name = 'main/home.html'

    def get_queryset(self):
        queryset = Tweet.objects.order_by('-id')
        return queryset
    

def conversation(request, tweet_id):
    return HttpResponse("You're looking at the part where people resond to it this is tweet %s." % tweet_id)

class Timeline(DetailView):
    template_name = 'main/timeline.html'
    queryset = Profile.objects.all()

    def get_object(self):
        UserName = self.kwargs.get("username")
        return get_object_or_404(Profile, username=UserName)
    

