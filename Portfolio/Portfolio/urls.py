"""Portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""


from django.contrib import admin
from django.urls import path, include
# from ToyMain import views
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls), # 관리자 계정
    # path('Main/', include('ToyMain.urls') , name='Main'),
    # path('', views.MainKr, name='MainKr'),   # 한국어

    # # 진행중 
    # path('home/', include('blog.urls'), name='Home'), # blog

    # 진행중 
    
    # path('', views.main, name='main'),   # blog
    path('blog/', include('blog.urls')), # blog
    # path('home/', include('blog.urls'), name='Home'), # blog
]


# path('blogMain', views.test, name ='blogMain' ), # blogMain

# path('en', views.MainEn, name='MainEn'), # 영어


"""
자 일단 blog 정리 

일단 기본 페이지부터 타고갈수있게 세팅 하자 

# 조건 ! 파이썬 방식을 고수하자 !! 
"""