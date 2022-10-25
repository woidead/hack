from django.shortcuts import render
import requests
from django.http import HttpResponse
from main.models import *
from urllib.request import HTTPRedirectHandler
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.


def main(request):
    sneakers_API = 'https://abdullaev012.pythonanywhere.com/'
    res = requests.get(sneakers_API)
    data = res.json()
    land = len(data)
    i = 0
    ii = []
    while i != land:
        i = i + 1
        ii.append(i)
    ii.insert(0, 0)
    ii.pop()
    sneakers_name = []
    description = []
    image = []
    price = []
    idd = []
    zipped_values = zip(sneakers_name, description, image, price)
    for y in ii:
        sneakers_name.append(data[y]['sneakers_name'])
        description.append(data[y]['description'])
        image.append(data[y]['image'])
        price.append(data[y]['price'])
        idd.append(data[y]['id'])
    return render(request, "index.html", {'zipped_values': zipped_values, })


def podrobno(request):
    return render(request, 'podrobno.html')


def onas(request):
    return render(request, 'onas.html')


def basket(request):
    return render(request, 'basket.html')


def signUp(request):
    if request.method == 'POST':
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            return HttpResponseRedirect('/')
    else:
        user = UserCreationForm()
    return render(request, 'auth.html', {'user': user})


def signin(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            form = AuthenticationForm()
            return render(request, 'auth.html', {'user': form})
    except UnboundLocalError:
        return render(request, 'a404.html')


def signout(request):
    logout(request)
    return HttpResponseRedirect('/')


def add_products(request, pk):
    sneakers_API = 'https://abdullaev012.pythonanywhere.com/'
    res = requests.get(sneakers_API)
    data = res.json()
    land = len(data)
    i = 0
    ii = []
    while i != land:
        i = i + 1
        ii.append(i)
    ii.insert(0, 0)
    ii.pop()
    idd = []
    zipped_values = zip(idd)
    for y in ii:
        idd.append(data[y]['id'])
    return render(request, "index.html", {'zipped_values': zipped_values })
        


# def addCart(request, pk):
#     try:
#         cart_session = request.session.get('cart_session', [])
#         cart_session.append(pk)
#         request.session['cart_session'] = cart_session
#         return HttpResponseRedirect('/')
#     except:
#         return render(request, 'error.html')
