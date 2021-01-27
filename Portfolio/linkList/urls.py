# blog\urls.py

from django.urls import path, re_path
from linkList import views
# from linkList.models import LinkList
# from django.views.generic import TemplateView, ListView, DetailView

app_name = 'linkList'

urlpatterns = [

    # photo
    path('', views.linkLV.as_view(), name='index'),
    path('<int:pk>', views.linkDV.as_view(), name='link_detail'),
    # path('photo/<int:pk>/', views.PhotoDV.as_view(), name='photo_detail'),

]

