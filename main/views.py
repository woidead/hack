import requests
from main.models import Client, Order
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from main.api import *
from collections import Counter
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
    id = []
    zipped_values = zip(sneakers_name, description, image, price, id)
    for y in ii:
        sneakers_name.append(data[y]['sneakers_name'])
        description.append(data[y]['description'])
        image.append(data[y]['image'])
        price.append(data[y]['price'])
        id.append(data[y]['id'])
    return render(request, "index.html", {'zipped_values': zipped_values})


def more(request, id):
    try:
        more = zipped_values.objects.get(id=id)
        return render(request, 'more.html', {'more': more})
    except:
        return render(request, 'error.html')

def addCart(request, pk):
    cart_session = request.session.get('cart_session', [])
    cart_session.append(pk)
    request.session['cart_session'] = cart_session
    return HttpResponseRedirect('/')

def cart(request):
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
    id = []
    sneakers_name = []
    description = []
    image = []
    price = []
    for y in ii:
        id.append(data[y]['id'])
        sneakers_name.append(data[y]['sneakers_name'])
        description.append(data[y]['description'])
        image.append(data[y]['image'])
        price.append(data[y]['price'])
    zipped_values = zip(id, sneakers_name, description, image, price)
    lists = list(zipped_values)
    cart_session = request.session.get('cart_session', [])
    count_of_product = len(cart_session)
    products_cart = []
    all_products_sum = 0
    for j in cart_session:
        for i in lists:
            if i[0] == j:
                products_cart.append(i)
                all_products_sum += i[4]
            else:
                print('----------------')
    
    product = Counter(products_cart)
    lst = []
    for p, c in product.items():
        lst.append([p,c])
    return render(request, 'cart.html',{'count_of_product': count_of_product, 'all_products_sum': all_products_sum , 'lst':lst} )

def removeCart(request, id):
    cart_session = request.session.get('cart_session', [])
    carts = cart_session
    carts.remove(id)
    request.session['cart_session'] = carts
    return HttpResponseRedirect('/cart')


def podrobno(request):
    return render(request, 'podrobno.html')



def more(request, id):
    try:
        idd = []
        for i in lists:
            if i[0] == id:
                idd.append(i)
        print(idd)
        return render(request, 'more.html', {'idd': idd})
    except:
        return render(request, 'error.html')





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


def order(request):
    cart_session = request.session.get('cart_session', [])
    if request.method == 'POST':
        client = Client()
        count_of_product = len(cart_session)
        client.name = request.POST.get('c_name')
        client.last_name = request.POST.get('c_lastname')
        client.number = request.POST.get('c_number')
        client.address = request.POST.get('c_addres')
        client.message = request.POST.get('c_message')
        cart_session = request.session.get('cart_session', [])
        client.save()
        products_cart = []
        all_products_sum = 0
        for j in cart_session:
            for i in lists:
                if i[0] == j:
                    products_cart.append(i)
                    all_products_sum += i[4]
            request.session['cart_session'] = []
        messages.error(request,'Заказ успешно отправлен', extra_tags='success')
        return HttpResponseRedirect('/cart')

# def order(request):
#     cart_session = request.session.get('cart_session', [])
#     if request.method == 'POST':
#         if len(cart_session) == 0:
#             messages.error(request, 'Ваша карзина пустая',  extra_tags='danger')
#             return HttpResponseRedirect('cart')
#         else:
#             customer = Client()
#             customer.name = request.POST.get('c_name')
#             customer.last_name = request.POST.get('c_lastname')
#             customer.number = request.POST.get('c_number')
#             customer.address = request.POST.get('c_addres')
#             customer.message = request.POST.get('c_message')
#             customer.save()
#             for i in range(len(cart_session)):
#                 order = Order()
#                 cart_session = request.POST.get('cart_session', [])
#                 cart_session_lst = cart_session
#                 set_list = set(cart_session_lst)
#                 product_names_and_counts = []
#                 for i in set_list:
#                     product = SneakersCard.objects.get(id = i)
#                     product_name = product.tittle
#                     count = cart_session_lst.count(i)
#                     products = f"{product_name}-{count}"
#                     product_names_and_counts.append(products)
#                     products_cart = SneakersCard.objects.filter(id__in= cart_session)
#                     all_products_sum = 0
#                     for i in products_cart:
#                         i.count = cart_session.count(i.id)
#                         i.sum = i.count * i.price
#                         all_products_sum += i.sum
#                     order.product = product_names_and_counts
#                     order.customer = customer
#                     order.total_price = all_products_sum
#                     order.phone = customer.number
#                     order.address = customer.address
#                     order.save()
#                 request.session['cart_session'] = []
#                 messages.error(request,'Заказ успешно отправлен', extra_tags='success')
#                 return HttpResponseRedirect('cart')


