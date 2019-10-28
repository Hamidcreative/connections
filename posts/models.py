
from django.db import models
from django.utils import timezone
from django.conf import settings


class Post(models.Model):
    author     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title      = models.CharField(max_length=100)
    status     = models.IntegerField(default=0)
    type       = models.IntegerField(default=0)
    content    = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    sent_on    = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
