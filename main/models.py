from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=10000)
    timestamp = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class site(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text =  models.CharField(max_length=420)
    verified = models.BooleanField()
    timestamp = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
