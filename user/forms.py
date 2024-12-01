from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["image","phone","gender","region","city","address","passport_id","birth_date","specialization","experience","service_type","meeting","user_type",'password1','password2','first_name','last_name']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["image","phone","gender","region","city","address","passport_id","birth_date",'first_name','last_name']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["phone","passport_id",'password1','password2']

