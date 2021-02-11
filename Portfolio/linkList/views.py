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


class linkCreateView(DetailView):
    # model = LinkList
    # template_name = 'linkList/link_detail.html'
    pass


class linkChangeLV(DetailView):
    # model = LinkList
    # template_name = 'linkList/link_detail.html'
    pass


class linkUpdateView(DetailView):
    # model = LinkList
    # template_name = 'linkList/link_detail.html'
    pass


class linkDeleteView(DetailView):
    # model = LinkList
    # template_name = 'linkList/link_detail.html'
    pass


# TAG
class TagCloudTV(TemplateView):
    """
    docstring
    """
    template_name = 'linkList/taggit/taggit_cloud.html'


class TaggedObjectLV(ListView):
    """
    docstring
    """
    model = LinkList
    template_name = 'linkList/taggit/taggit_linkList_list.html'

    def get_queryset(self):
        """
        docstring
        """
        return LinkList.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        """
        docstring
        """
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context
