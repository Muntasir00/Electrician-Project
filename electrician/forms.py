from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms
from django.contrib.auth.models import User
from .models import Order




class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1','password2']



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['name','email','message']
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.TextInput(attrs={'class': 'form-control'}),
            'message':forms.Textarea(attrs={'cols': 40, 'rows': 10}),
            
        }
        
 

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'electrician_id','address',
                    'postal_code', 'city']