from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import TwitterUserModel


class RegistrationForm(UserCreationForm):
    displayname = forms.CharField(max_length=60)
    bio = forms.CharField(max_length=255, widget=forms.Textarea)

    class Meta:
        model = TwitterUserModel
        fields = ('displayname', 'username', 'password1', 'password2', 'bio')


class EditUserForm(UserChangeForm):
    pass
