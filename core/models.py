from django.db import models
from django.contrib.auth.models import AbstractUser

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class VideoTutorial(models.Model):
    title = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    # video_url = models.URLField()
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title

class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='core_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
        related_query_name='core_user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='core_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
        related_query_name='core_user'
    )

    def __str__(self):
        return self.name


