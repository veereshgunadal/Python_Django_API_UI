from django.shortcuts import render,redirect

from django.shortcuts import HttpResponse

from app1.models import Product,User
from app1.forms import UserForm

import json

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def register_check(request):
    form = UserForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
        return redirect("login")
    if form.errors:
        print(form.errors)
        res_data = json.dumps({'errorcode':400, 'errormessage':'please retry this username already exist'})
        return HttpResponse(res_data, content_type = 'application/json')
    
def login_check(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
    try:
        data_obj = User.objects.get(username = username)
        password_db = data_obj.password
        if password == password_db:
            return render(request, 'homeafterlogin.html', {'username':username})    
        else:                        
            res_data = json.dumps({'errorcode':400, 'errormessage':'invalid credentials'})
            return HttpResponse(res_data, content_type='application/json')
    except:
        res_data = json.dumps({'errorcode':404, 'errormessage':'user not found'})
        return HttpResponse(res_data, content_type='application/json')

def product(request):
    data_obj = Product.objects.all()
    return render(request, 'product.html', {'products':data_obj})