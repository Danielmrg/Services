from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude=['user','username']
    

class ExpertForm(forms.ModelForm):
    class Meta:
        model = Expert
        fields = '__all__'
        exclude=['user','username']

class RegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = {'username','email','password1','password2'}
        
        
class ReqForm(forms.ModelForm):
    class Meta:
        model = Request_srv
        fields = '__all__'
        widgets = {'expert': forms.HiddenInput(),'customer': forms.HiddenInput()}

        