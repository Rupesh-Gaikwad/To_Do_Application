from django import forms
from django.contrib.auth.models import User
from to_do_App.models import Tasks
from django.forms import fields, widgets
from django.utils.translation import ugettext_lazy as _

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'password']
        labels = {
            'first_name': 'First Name',
            'last_name' : 'Last Name',
        }
        help_texts = {
            'username': '',
        }
        widgets = {
            'password': forms.widgets.PasswordInput(),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        help_texts = {
            'username': '',
        }
        widgets = {
            'password': forms.widgets.PasswordInput(),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['username','title', 'description', 'task_starts_at', 'task_ends_at',]
        
