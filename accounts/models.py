from django.db import models
from django.utils import timezone
from django.conf import settings


class Account(models.Model):
    user_ac    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name       = models.CharField(max_length=100) # This can be the name of a LinkedIn Profile, Page or Group.
    avatar     = models.CharField(max_length=150) # This is the avatar of a profile, page, or group.
    followers  = models.IntegerField(default=0)   # This is the total number of followers a profile, page, or group has.
    status     = models.IntegerField(default=0)   # not in use
    type       = models.IntegerField(default=0)   # This can be a profile, page, or group
    about      = models.TextField()               # not in use
    created_at = models.DateTimeField(default=timezone.now) # This is the date the account is connected to Status.
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name