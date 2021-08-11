from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile
class UserRegisterForm(UserCreationForm): #inheriting from UserCreationForm class

    email=forms.EmailField()

    class Meta:
        model=User #we specify the database, where we want to store the details.
        fields=['username','email','password1','password2'] #fields req in form to display.


class UserUpdateForm(forms.ModelForm):

    email=forms.EmailField()

    class Meta:
        model=User #we specify the database, where we want to store the details.
        fields=['username','email',] #fields req in form to display.


class ProfileUpdateForm(forms.ModelForm):


    class Meta:
        model=profile #we specify the database, where we want to store the details.
        fields=['image'] #fields req in form to display.

