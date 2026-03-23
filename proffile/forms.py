from main.models import Time, Author, Article
from django.forms import ModelForm, TextInput, Textarea, FileInput
from django import forms

# class AuthorForm(ModelForm):
#     class Meta:
#         model = Author
#         fields = ['nickname','password', 'info_about_author']

#         widgets = {
#             'nickname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nickname'}),
#             'password': TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
#             'info_about_author': Textarea(attrs={'class': 'form-control', 'placeholder': 'Info about you'})
#         }


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    widgets = {
        'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        'password1': TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        'password2': TextInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        
    }

class LoginForm(forms.Form):

    username = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)

        