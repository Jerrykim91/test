
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
# from django.db import connection
# cursor = connection.cursor()
# from .models import join # 모델 호출 
# User = get_user_model() # 변수 선언

# Create your views here.


"""
서버를 어떤 방식으로 만들지 생각 해보자 
일단을 프로젝트들을 업로드 할건데 

로그인이 필요한 작업은 음식, gdp 그외에는 결과만 보여주면 되는 구조 

결과만 보여주는거는 어떻게 보여 줄건데 -> 분석이나 시각화는 되어 있어야하는데 ... 


템플릿 사이트 
https://html5up.net/
https://mdbootstrap.com/freebies/

[참고용] https://all-free-download.com/free-website-templates/

"""

@csrf_exempt
def Main(request):
    '''
    Main 
    '''
    if request.method == 'GET':
        return render(request,'index_kr.html')



# txt = """

#     <html>
#     <head><title>%s</title></head>
#     <body>
#     <h1>%s</h1><p>%s</p>
#     </body>
#     </html>
#       """% (
# '제리 | test 진행중',
# '정상동작 합니다.',
# '다음 스탭으로 진행합니다!'
# )


# @csrf_exempt
# def Main(request):
#     '''
#     테스트 버전 Dummy
#     '''
#     return HttpResponse(txt)


