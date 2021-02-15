
from django.views.generic import ListView, DetailView
from melog.models import Album, Photo


# Create your views here.

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
