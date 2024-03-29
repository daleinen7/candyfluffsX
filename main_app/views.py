from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Banner, AnimeCon

# Create your views here.


def home(request):
    products = Product.objects.all()
    banners = Banner.objects.all()
    return render(request, 'home.html',  {'products': products, 'banners': banners})


def about(request):
    return render(request, 'about.html')


def conventions(request):
    return render(request, 'conventions.html')


class ProductsList(ListView):
    model = Product
    template = 'product_list.html'


class ProductDetail(DetailView):
    model = Product
    template = 'product_detail.html'


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
