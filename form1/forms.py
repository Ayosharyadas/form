from django import forms
from django.core import validators
def value_size(value):
    if len(value)<6:
        raise forms.ValidationError("this pasword is too short")



class EmployeeForm(forms.Form):
     firstname = forms.CharField(label="Enter first name",max_length=50)
     lastname  = forms.CharField(label="Enter last name", max_length = 100)
     email = forms.EmailField(help_text='write your email', )
     Address = forms.CharField(required=False, )
     Technology = forms.CharField(initial='Django', disabled=True, )
     age = forms.IntegerField()
     password = forms.CharField(widget=forms.PasswordInput,validators = [value_size,])
     re_password = forms.CharField(help_text='renter your password', widget=forms.PasswordInput)

