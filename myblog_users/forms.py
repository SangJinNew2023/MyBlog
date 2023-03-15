from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProfileModel
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField() #add the email field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # remove the help_text on the signup window
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    # remove the help_text on the signup window
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email']:
            self.fields[fieldname].help_text = None

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['image']


