import django_filters
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import *


class RegisterUserForm(UserCreationForm):
  class Meta:
    model =get_user_model()
    fields=['email','password1','password2']
class CompanyForm(forms.ModelForm):
  class Meta:
    model =Company
    exclude=['user',]
class ResumeForm(forms.ModelForm):
  class Meta:
    model =Resume
    exclude=['user',]
class JobForm(forms.ModelForm):
  class Meta:
    model =Job
    exclude=('user','company')  
         
class UpdateJobForm(forms.ModelForm):
  class Meta:
    model =Job
    exclude=('user','company')       
class JobFilter(django_filters.FilterSet):
  title=django_filters.CharFilter(lookup_expr='icontains')
  class Meta:
    model =Job
    fields=['title','city','job_type','industry']
    widgets ={
          'city':forms.Select(attrs={'class': 'form-control'}) ,
          'job_type':forms.Select(attrs={'class': 'form-control'}) 

       }
class reviewss(forms.ModelForm):
    class Meta:
       model = review
       fields = ['text']
       widgets ={
          'text':forms.TextInput(attrs={'class':'input'}), 
       }
       labels={
          'text':'add a comment'
       }     