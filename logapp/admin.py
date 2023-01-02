from django.contrib import admin
from .models import Certificationmodel, Registration, Topic
# Register your models here.
admin.site.register(Registration)
admin.site.register(Topic)
admin.site.register(Certificationmodel)