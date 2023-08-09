
# Create your views here.


from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def index(request):
    return render(request,"index.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('base')
        else:
            print('invalid')
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['confirm_password']


        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect("register")

            else:
                user=User.objects.create_user(username=username,password=password)

                user.save()
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect("register")



    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def base(request):
    return render(request,'base.html')

def form(request):
    return render(request,'form.html')


