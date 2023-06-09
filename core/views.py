from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth import logout
from django.contrib import messages

from .models import Category, Service, VideoTutorial


def homepage(request):
    categories = Category.objects.all()
    services = Service.objects.all()
    return render(request, 'homepage.html', {'categories': categories, 'services': services})

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def tutorials(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    tutorials = VideoTutorial.objects.filter(service=service)
    return render(request, 'tutorials.html', {'services': service, 'tutorials': tutorials})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered.')
            return redirect('core:login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('core:homepage')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('core:homepage')
