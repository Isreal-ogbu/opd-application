from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Registration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    USER_TYPE = (
        ('0', 'Patient'),
        ('1', 'Doctor'),
    )
    usertype = models.CharField(choices=USER_TYPE, max_length=50, null=True)
    mobile_number = models.CharField(('phone number'), max_length=10, unique=True)
    gender = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='images/', null=False)
    address = models.CharField(('user address'), max_length=200, null=True)
    city = models.CharField(('city'), max_length=100)
    state = models.CharField(('state'), max_length=100)
    postal_code = models.IntegerField(('postal_code'))

    def save(self, *args, **kwargs):
        return super(Registration, self).save(*args, **kwargs)

class Topic(models.Model):
    health_case = (('1', 'Mental Health'), ('2', 'Health Disease'), ('3', 'covid-19'), ('4', 'Immunization'))
    Title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='topic/', null=False)
    category = models.CharField(choices=health_case, max_length=20, null=True)
    contents = models.TextField()
    summary = models.TextField()

    def __str__(self):
        """return a string representation of the text"""
        if len(self.Title) > 50:
            return self.Title[:15] + "..."

    def __str__(self):
        """return a string representation of the text"""
        if len(self.summary) or len(self.contents) > 50:
            return self.summary[:15] + "..." or self.contents[:15] + '....'

class Certificationmodel(models.Model):
    company_name = models.CharField(max_length=50)
    issuer_name = models.CharField(max_length=50)
    reciever_name = models.CharField(max_length=50)
    reason = models.CharField(max_length=1000)