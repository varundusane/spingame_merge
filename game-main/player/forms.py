from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Player



class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        del self.fields['password2']

    username = forms.CharField(
        max_length=200,
        required=True,
        # help_text='Enter UserName',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
    )
    nickname = forms.CharField(
        max_length=200,
        required=True,
        # help_text='Enter NickName',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Nickname'}),
    )
    password1 = forms.CharField(
        # help_text='Enter Password',
        label="Enter Password",
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Strong Password'}),
    )
    # check = forms.BooleanField(required=True)
    class Meta:
        model = User
        fields = [
        'username', 'nickname', 'password1',  
        ]    



