from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Maincommunity
from django.views.decorators.csrf import csrf_exempt
from WordWarAPI.checkValidWord import isValidWord

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')
        else:
            return HttpResponse('사용자명이 이미 존재합니다.')
    else:
        form = UserForm()
        return render(request, 'auth/adduser.html', {'form': form})

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'auth/login.html', {'form': form})

def Community_index(request):
  Cdata = Maincommunity.objects.all()
  return render(request, 'default.html', {'Cdata': Cdata})

def index(request):
    return render(request, 'default.html')

def nextword(request):
    word = request.GET['word']


def validword(request):
    t = request.GET['word']
    flag = isValidWord(t)
    return JsonResponse({'total': flag,'echo':t})

#To be Removed
@csrf_exempt
def logintest(request):
    if request.method == "POST":
        return JsonResponse({'status': 'Success'})
