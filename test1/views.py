from django.shortcuts import render, redirect
from .models import Product, Contact_Query
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.

def home(request):
    product_info = Product.objects.all()
    print(product_info)
    return render(request, 'test1/home.html',{'product_info':product_info})
    # return HttpResponse('<h1>Home Page<\h1>')

def findproduct(request):
    if request.method == 'POST':
        x = request.POST.get('prod_search')
        mydata = Product.objects.filter(Q(Product_Name__icontains = x) | Q(Product_Category__icontains = x))
        if mydata:
            return render(request, 'test1/home.html',{'product_info':mydata})
        else:
            return render(request, 'test1/home.html',{'warning':"No Product found!!"})

def contact(request):
    if request.method == 'GET':
        return render(request, 'test1/contact.html')
    else:
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('message')
        new_data = Contact_Query(name=a, email=b, message=c)
        new_data.save()
        return render(request, 'test1/contact.html', {'x':"Message sent Successfully!"})

def products(request):
    product_info = Product.objects.all()
    paginator = Paginator(product_info, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'test1/product.html', {"page_obj": page_obj})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'test1/loginuser.html', {'form':AuthenticationForm()})
    else:
        a = request.POST.get('username')
        b = request.POST.get('password')
        user = authenticate(request, username=a, password=b)
        if user is None:
            return render(request, 'test1/loginuser.html', {'form':AuthenticationForm(), 'error':"Invalid Credentials!! Try Again...."})
        else:
            login(request, user)
            return redirect('home')
    
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'test1/signupuser.html', {'form':UserCreationForm()})
    else:
        a = request.POST.get('username')
        b = request.POST.get('password1')
        c = request.POST.get('password2')
        if b == c:
            if(User.objects.filter(username = a)):
                return render(request, 'test1/signupuser.html', {'form':UserCreationForm(), 'error':"User Name Already taken!! Try Again with some new User Name...."})
            else:
                user = User.objects.create_user(username = a, password = b)
                user.save()
                login(request, user)
                return redirect('home')
        else:
            return render(request, 'test1/signupuser.html', {'form':UserCreationForm(), 'error':"Password Mismatch!! Try Again...."})
    
def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        return redirect('home')