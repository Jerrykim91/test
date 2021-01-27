from django.shortcuts import render

# 1. 클래스형 제네릭뷰
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
from linkList.models import LinkList

# Create your views here.


class linkLV(ListView):
    model = LinkList
    template_name = 'linkList/link_list.html'


class linkDV(DetailView):
    model = LinkList
    template_name = 'linkList/link_detail.html'
