import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from django.shortcuts import render
from main.models import Product
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'npm': '2206083514',
        'class': 'PBP A',
        'products': products,
        'last_login': request.COOKIES['last_login'],
        'name1': "ArmsKore Coil Gun",
        'name2': "Reinforced Power Drills",
        'name3': 'Pickaxe',
        'amount1': '11',
        'amount2': '20',
        'amount3': '68',
        'description1': 'A miniaturized electromagnetic coilgun surrounded by technological components as part of its bulky exterior which fires projectiles capable of piercing through solid rock and enemies.',
        'description2': 'The Drillers mobility tool. They are a pair of massive handheld drills mounted up to the Drillers forearms.',
        'description3': 'The Pickaxe is a fundamental Support Tool available to every class. It allows the player to shape the environment around them.',
        'category1':'Secondary Weapon',
        'category2':'Support Tool',
        'category3':'Support Tool',
        'stats1a':'Damage : 130',
        'stats1b':'Magazine Size : 1',
        'stats1c':'Max Ammo : 640',
        'stats1d':'Reload Time : 2.5s',
        'stats1e':'Charged Shot Ammo Use : 40',
        'stats2a': 'Damage : 5 Melee',
        'stats2b': 'Max Fuel : 38',
        'stats2c': 'Fear Factor : 50%',
        'stats2d': 'Mining Rate : 1.5',
        'stats2e': 'Armor Break : 10000%',
        'stats3a': 'Damage : 27.5 Melee',
        'stats3b': 'Armor Breaking : 150%',
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response