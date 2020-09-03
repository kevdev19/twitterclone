from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import TwitterUserModel


class RegistrationForm(UserCreationForm):
    displayname = forms.CharField(max_length=60)

    class Meta:
        model = TwitterUserModel
        fields = ('displayname', 'username', 'password1', 'password2', )
