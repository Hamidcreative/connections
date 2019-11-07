
from django.db import models
from django.utils import timezone
from django.conf import settings


class Postssss(models.Model):
    author     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title      = models.CharField(max_length=100) # Name
    status     = models.IntegerField(default=0)
    interval   = models.IntegerField(default=0) # This is the day interval of an update.
    frequency  = models.IntegerField(default=0) # This is the total number of times an update will be published
    time       = models.DateTimeField(default=timezone.now) # This is the time of the day an update will be published.
    type       = models.IntegerField(default=0) # Account like profile , page , group
    hashtag    = models.CharField(max_length=150) # This is the first comment of an update
    comment    = models.TextField(default=0)
    image      = models.CharField(max_length=100)
    content    = models.TextField()             # Update
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    sent_on    = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
