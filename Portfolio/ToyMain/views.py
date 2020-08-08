
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

# 로그인 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate as auth
from django.contrib.auth import login as login
from django.contrib.auth import logout as logout
from django.contrib.auth import get_user_model

# db
# from .models import join # 모델 호출 
User = get_user_model() # 변수 선언

# Create your views here.


@csrf_exempt
def Main(request):
    '''
    Main 
    '''
    if request.method == 'GET':
        return render(request,'Main.html')
