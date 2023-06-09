from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('services/', views.services, name='services'),
    path('categories/', views.categories, name='categories'),
    path('services/<int:service_id>/tutorials/', views.tutorials, name='tutorials'),
     # User Registration
    path('register/', views.register, name='register'),

    # User Login
    path('login/', views.user_login, name='login'),

    # User Logout
    path('logout/', views.user_logout, name='logout'),
]