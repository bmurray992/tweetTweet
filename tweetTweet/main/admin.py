from django.contrib import admin
from .models import Profile, Tweet

# Register your models here
class TweetInline(admin.TabularInline):
    model = Tweet
    extra = 2

class TweetAdmin(admin.ModelAdmin):
    model = Tweet
    list_display = ('tweet_creator', 'tweet_date')
    list_filter = ['tweet_date',]
    
admin.site.register(Tweet, TweetAdmin)