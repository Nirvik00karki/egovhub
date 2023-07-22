from django.contrib import admin
from .models import Service, Category, VideoTutorial,CustomUser

admin.site.register(Service)
admin.site.register(Category)
admin.site.register(VideoTutorial)
admin.site.register(CustomUser)