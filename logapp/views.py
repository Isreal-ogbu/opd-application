from decimal import Context
from django.shortcuts import render, redirect
from django.contrib.auth import logout,login
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import RegistrationForm, topicform, certificationform
from django.contrib.auth.decorators import login_required
from .models import Certificationmodel, Topic


def home(request):
    datas = Topic.objects.all()
    context = {
        "datas": datas
    }
    return render(request, 'blog/index.html', context=context)

# Create your views here.
def Logout_views(request):
    """log out function"""
    logout(request)
    return HttpResponseRedirect(reverse('login'))


@csrf_exempt
def register(request):
    """register new user"""
    if request.method != 'POST':
        """return a blank creation form"""
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            context={
        'form': form
    }
            return render(request, 'accounts/success.html', context=context)
    context={
        'form': form
    }
    return render(request, 'accounts/register.html', context=context)

@login_required
def create_post(request):
    if request.method == "POST" :
        print(request.user)
        form = topicform(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.owner = request.user
            new.save()
            return HttpResponseRedirect(reverse('Home'))
    else:
        form = topicform()
    context = {
        "form": form
    }
    return render (request, 'blog/doctor.html', context=context)

def certificate(request):
    if request.method == "POST":
        form1 = certificationform(request.POST)
        if form1.is_valid():
            form1.save()
    else:
        form1 = certificationform()
    form = Certificationmodel.objects.all()
    print(form)
    context = {
        "form": form,
        "form1": form1
    }  
    return render (request, 'certificate/cert.html', context=context)
