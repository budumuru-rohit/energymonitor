from django.shortcuts import render,redirect
from django.http import HttpResponse
#inbuilt lib for signup
from django.contrib.auth.models import User
#for sending message
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home_view(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['pass1']
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect("home")
            #return render(request,"authentication/good.html")
        else:
            messages.error(request,"Bad Credentials")
            return redirect('home')
    return render(request,"authentication/index.html")
def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        fname=request.POST.get('firstName')
        lname=request.POST.get('lastName')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your Acount has been successfully created.")
        return redirect("home")
    return render(request,"authentication/signup.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect('home')
def dash(request):
    return render(request,"authentication/dashboard.html")