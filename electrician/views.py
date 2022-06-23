from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *
from .models import Electrician, Order, OrderItem
from .forms import OrderCreateForm


    
def home(request):
    electricians = Electrician.objects.all()
    return render(request,'home.html',{'electricians':electricians})

def electrician(request):
    electricians = Electrician.objects.all()
    return render(request,'electrician.html',{'electricians':electricians})

def about(request):
    electricians = Electrician.objects.all()
    return render(request,'about.html',{'electricians':electricians})



def registerpage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,'Account was Created for '+ username)
            login(request, user)
            return redirect('home')


    context={'form':form}
    return render(request,'account/register.html',context)




def userlogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request,'Username or Password incorrect.')
    context={}
    return render(request,'account/login.html',context)




def logoutuser(request):
    logout(request)
    return redirect('login')



def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form = form.save()
            messages.info(request,'You have sent your message successfuly.')
            return redirect('contact')
    context={'form':form}
    return render(request,'contract.html',context)

def order_create(request):
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            
        return render(request,'created.html',{'order':order})
    
    else:
        form = OrderCreateForm()
        return render(request,'create.html',{'form':form})