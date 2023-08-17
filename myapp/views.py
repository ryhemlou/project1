from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature


from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Error
from allauth.socialaccount import providers

from django.contrib.auth import login


from allauth.socialaccount.models import SocialAccount





# Create your views here.

def index(request):
    features=Feature.objects.all()
    return render(request,'index.html',{'features' : features})



def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html',{'amount':amount_of_words})



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            #we need to check if the email the user is providing already exists or not in our database
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else :
                #if any of them is false we need to creat the user in our database
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save
                return redirect('login')
        else :
            messages.info(request, 'Password Not The Same')
            return redirect('register')
    else:
        return render(request,'register.html')




def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)

        #now we want to check if the user give us the wrong informations ,which are not in our database?
        #(if the user is really registred or not)
        if user is not None:
            #if we login seccefully we will find the main page (the page of index.html)
            auth.login(request, user)
            return redirect('/')
        else :
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def counter1(request):
    posts=[1,2,3,4,5,'ryhem','sadok']
    return render(request, 'counter1.html', {'posts': posts})

#dynamic url
def post(request, pk):
    return render(request, 'post.html', {'pk':pk})






