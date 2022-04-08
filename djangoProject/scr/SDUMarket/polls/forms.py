from django import forms
from django.forms import ModelForm
from .models import Room



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


