
# from django.shortcuts import redirect
# from django.http import HttpResponse, HttpResponseNotFound
# from django.views.decorators.csrf import csrf_exempt

# # 로그인

# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate as auth
# from django.contrib.auth import login as login
# from django.contrib.auth import logout as logout
# from django.contrib.auth import get_user_model

# # 1. 클래스형 제네릭뷰

from django.views.generic import ListView, DetailView
# from django.views.generic.dates import ArchiveIndexView
# # from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
# # from django.views.generic.dates import DayArchiveView, TodayArchiveView

# # 2-1. 테이블 조회를 위한 모델 임포트
from melog.models import Album, Photo

# # 2-2. 템플릿 뷰
# from django.views.generic import TemplateView

# # 4. search
# from django.views.generic import FormView
# from blog.forms import PostSearchForm
# from django.shortcuts import render  # render : 위에 제거하고 다시 작성


# # Create your views here.

"""
urls.py 에서 바로 model 지정가능 함 책 207 페이지 참조 
"""

class AlbumLV(ListView):
    template_name = 'photo/album_list.html'
    model = Album


class AlbumDV(DetailView):
    template_name = 'photo/album_detail.html'
    model = Album


class PhotoDV(DetailView):
    template_name = 'photo/photo_detail.html'
    model = Photo
