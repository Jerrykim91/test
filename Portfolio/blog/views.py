from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

# 로그인

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate as auth
from django.contrib.auth import login as login
from django.contrib.auth import logout as logout
from django.contrib.auth import get_user_model

# 1. 클래스형 제네릭뷰

from django.views.generic import ListView, DetailView,CreateView 
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
# 추가 
# from django.views import generic
from django.urls import reverse
from .forms import BlogForm

# 2-1. 테이블 조회를 위한 모델 임포트
from blog.models import Post

# 2-2. 템플릿 뷰
from django.views.generic import TemplateView

# 3. comment
from django.conf import settings

# 4. search
from django.views.generic import FormView
from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render  # render : 위에 제거하고 다시 작성


# Create your views here.

 # TemplateView
class HomeView(TemplateView):
    """
    docstring
    """
    template_name = 'blog/home.html'


#ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2  # 한페이지에 보여주는 객체 리스트의 개수


class AboutDV(TemplateView):

    model = Post
    template_name = 'blog/post_about_me.html'

    # def get_context_data(self, **kwargs):
    #     context = super(indexView, self).get_context_data(**kwargs)
    #     return context


# DetailView
class PostDV(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        """
        docstring
        """
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}" #ex)http://127.0.0.1:8000/blog/post/99
        context['disqus_title'] = f"{self.object.slug}"
        return context


# ArchiveView
class PostAV(ArchiveIndexView):
    """
    docstring
    """
    model = Post
    date_field = 'modify_dt'

# # 추가 
# class PostCreate(CreateView):
#     model = Post
#     template_name = 'blog/posting.html'
#     feilds = ['title', 'description','content','tags'] # 모델에서 가져 올 필드명 작성
#     template_name_suffix='_create'
#     #사용하는 탬플릿 명을 '모델명_create.html'로 바꾼다는 의미. 접미사만 바꾼다.
#     #기본 탬플릿은 '모델명_form.html'로 나타난다.
        # form_class = ReviewForm
#     def form_valid(self, form):  # 폼에 이상이 없으면 실행.
#         temp = form.save(commit=False)  # 임시 저장. 폼 외의 다른 내용을 조작하고 싶을 때 사용한다.
#         # 조작
#         temp.save()  # 최종 저장
#         return super().form_valid(form)
        
#     def get_success_url(self):  # 기존 함수를 덧쓴다. 작성 후에 해당 글을 보여주게끔.
#         return reverse('pool:detail', kwargs={'pk': self.object.blog.pk})

class PostYAV(YearArchiveView):
    """
    docstring
    """
    model = Post
    date_field = 'modify_dt'
    make_object_list = True

class PostMAV(MonthArchiveView):
    """
    docstring
    """
    model = Post
    date_field = 'modify_dt'

class PostDAV(DayArchiveView):
    """
    docstring
    """
    model = Post
    date_field = 'modify_dt'

class PostTAV(TodayArchiveView):
    """
    docstring
    """
    model = Post
    date_field = 'modify_dt'


# TAG
class TagCloudTV(TemplateView):
    """
    docstring
    """
    template_name = 'blog/taggit/taggit_cloud.html'


class TaggedObjectLV(ListView):
    """
    docstring
    """
    template_name = 'blog/taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        """
        docstring
        """
        return Post.objects.filter(tags__name= self.kwargs.get('tag'))


    def get_context_data(self, **kwargs):
        """
        docstring
        """
        context = super().get_context_data(**kwargs)    
        context['tagname'] = self.kwargs['tag']
        return context


# Search
class SearchFormView(FormView):     
    """
    docstring
    """
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self,form):
        """
        docstring
        """
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains = searchWord) | Q(description__icontains = searchWord) | Q(content__icontains = searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list


        return render(self.request, self.template_name, context) # No Redirection

"""
https://velog.io/@hwang-eunji/django-views-%ED%95%A8%EC%88%98%ED%98%95-vs-%ED%81%B4%EB%9E%98%EC%8A%A4%ED%98%95-%EC%A0%9C%EB%84%A4%EB%A6%AD

# 이미지 - 참고용 블로그
https://dheldh77.tistory.com/entry/Django-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%97%85%EB%A1%9C%EB%93%9C
"""


