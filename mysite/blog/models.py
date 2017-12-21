from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default = 1) #django 2.0 te eka req
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now = True)
    published_date = models.DateTimeField(auto_now_add = True, blank = True, null = True) #auto_now = jokhun first time create hobe jeta non editable, auto_now_add = everytime update korle time

#    def publish(self):
#        self.published_date = timezone.now()
#        self.save()

    def __str__(self):
        return self.title
