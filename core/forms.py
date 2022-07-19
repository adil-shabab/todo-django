from django import forms
from django.forms import ModelForm, TextInput
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'

class UpdateForm(forms.ModelForm):
    required_css_class = 'required-field'
    error_css_class = 'error-field'
    title = forms.CharField(widget=forms.TextInput(attrs={"class": 'span form-control rounded'}))
    class Meta:
        model = Tasks
        fields = ['title']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username' : TextInput(attrs={'class': 'field rounded'}),
            'email' : TextInput(attrs={'class': 'field rounded'}),
        }