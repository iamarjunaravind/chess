from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from .models import Enquire, Additional


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            hiuser = User.objects.get(username=username)
            print(hiuser)
            if user is not None:
                auth.login(request, user)
                print(hiuser)
                return render(request, "index.html", {'username': request.user.username})
            else:
                messages.warning(request, "invalid credentials")
                return redirect('/credentials/login')
        else:
            pass
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['cpassword']
        if password == confirm_password:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return redirect('/credentials/login/')
    return render(request,'register.html')


def enquire(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        highedu = request.POST['highedu']
        course = request.POST['course']

        enquire = Enquire(name=name, email=email, highedu=highedu, course=course)
        enquire.save()

        if enquire is not None:
            return redirect('/credentials/formsuccess')



    return render(request,'enquiry.html')


def formsuccess(request):
    return render(request,'formsuccess.html')