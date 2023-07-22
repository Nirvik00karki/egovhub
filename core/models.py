from django.db import models
from django.contrib.auth.models import AbstractUser

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey('core.Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class VideoTutorial(models.Model):
    title = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    video_url = models.URLField(default='https://www.example.com/default_video_url/')
    video = models.FileField(upload_to='videos/', default=False)

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    user_id = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.username} (User ID: {self.user_id})'



