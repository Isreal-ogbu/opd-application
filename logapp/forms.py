from dataclasses import fields
from tkinter import Widget
from xml.dom.minidom import Attr
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    Choices = (('1', "Patient"), ('K', "Doctor"))
    widgets = {"user": forms.CharField(widget=forms.Select(choices=Choices), max_length=2)}
    user = forms.CharField()
    mobile_number = forms.CharField(max_length=10)
    gender = forms.CharField()
    profile_image = forms.ImageField()
    address = forms.CharField(max_length=200)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    class Meta:
        model = User
        fields = ['user','username', 'first_name', 'last_name', 'email', 'profile_image', 'address', 'city', 'state', 'postal_code', 'password1', 'password2']

class topicform(forms.ModelForm):
    Title = forms.CharField(max_length=50)
    image = forms.ImageField()
    category = forms.CharField(max_length=20)
    contents = forms.Textarea()
    summary = models.TextField()
    class Meta:
        model = Topic
        fields = ['Title', 'owner', 'image', 'category', 'contents', 'summary']
        labels = {'text': '' }
    
class certificationform(forms.ModelForm):
    company_name = forms.CharField(max_length=50)
    issuer_name = forms.CharField(max_length=50)
    reciever_name = forms.CharField(max_length=50)
    reason = forms.CharField(max_length=1000)

    class Meta:
        model = Certificationmodel
        fields = '__all__'
