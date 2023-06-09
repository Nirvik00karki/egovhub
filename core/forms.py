from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    # Add any custom fields or overrides here

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')  # Customize the fields as per your requirements


class CustomAuthenticationForm(AuthenticationForm):
    # Add any custom fields or overrides here

    class Meta(AuthenticationForm.Meta):
        model = User
