from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import TODO
from django.contrib.auth import authenticate, login as auth_login ,logout
from django.contrib.auth.decorators import login_required



def signup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(name,email,password)
        my_user=User.objects.create_user(name,email,password)
        my_user.save()
        return redirect('/login')

    return render(request, 'todo/signup.html')


def login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        print(name,password)
        userr=authenticate(request,username=name,password=password)
        if userr is not None:
            auth_login(request, userr)
            return redirect('/todopage')
        else: 
            return redirect('/login')

    return render(request, 'todo/login.html')




@login_required(login_url='/login')
def todo(request):
    if request.method=='POST':
        title=request.POST.get('title')
        print(title)
        obj=models.TODO(title=title,user=request.user)
        obj.save()
        res=models.TODO.objects.filter(user=request.user).order_by('-date')
        return redirect('/todopage',{'res':res})

    res=models.TODO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo/todo.html',{'res':res})




@login_required(login_url='/login')
def edit_todo(request,srno):
    if request.method=='POST':
        title=request.POST.get('title')
        print(title)
        obj=models.TODO.objects.get(srno=srno)
        obj.title=title
        obj.save()
        user=request.user
        return redirect('/todopage')
    
    obj=models.TODO.objects.get(srno=srno)
    return render(request, 'todo/edit_todo.html',{'obj':obj})




@login_required(login_url='/login')
def delete_todo(request,srno):
    obj=models.TODO.objects.get(srno=srno)
    obj.delete()
    return redirect('/todopage')


def signout(request):
    logout(request)
    return redirect('/login')