from django.db import models
from accounts.models import Profile
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

# Create your models here.
class Tweet(models.Model):
    tweet_content = models.CharField(max_length = 255)
    tweet_date = models.DateTimeField('date published')
    tweet_creator = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return "%s tweeted at %s" % (self.tweet_creator, self.tweet_date)