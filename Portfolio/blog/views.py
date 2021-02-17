from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

# 로그인
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate as auth
# from django.contrib.auth import login as login
# from django.contrib.auth import logout as logout
# from django.contrib.auth import get_user_model

# 1. 클래스형 제네릭뷰
from django.views.generic import ListView, DetailView  
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

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

# 6. App Extend 
from django.views.generic import CreateView, UpdateView, DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin # login_required 기능 
from django.urls import reverse_lazy
from Portfolio.views import OwnerOnlyMixin


# Create your views here.





#ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 5  # 한페이지에 보여주는 객체 리스트의 개수


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
        context['disqus_id']    = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url']   = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}" #ex)http://127.0.0.1:8000/blog/post/99
        context['disqus_title'] = f"{self.object.slug}"
        return context


# ArchiveView
class PostAV(ArchiveIndexView):
    """
    docstring
    """
    model = Post
    date_field = 'modify_dt'

# App Extend
class PostCreateView(LoginRequiredMixin,CreateView):
    model          = Post
    template_name  = 'blog/post_form.html'
    fields         = ['title', 'slug','description','content','tags'] # 모델에서 가져 올 필드명 작성
    initial        = {'slug':'Auto-Filling-Do-Not-input'}
    success_url    = reverse_lazy('blog:index') # redirect

    def form_valid(self, form):  # 폼에 이상이 없으면 실행.
        form.instance.owner = self.request.user
        return super().form_valid(form)



def show_category(request,hierarchy= None):
    category_slug = hierarchy.split('/')
    category_queryset = list(Category.objects.all())
    all_slugs = [ x.slug for x in category_queryset ]
    parent = None
    for slug in category_slug:
        if slug in all_slugs:
            parent = get_object_or_404(Category,slug=slug,parent=parent)
        else:
            instance = get_object_or_404(Post, slug=slug)
            breadcrumbs_link = instance.get_cat_list()
            category_name = [' '.join(i.split('/')[-1].split('-')) for i in breadcrumbs_link]
            breadcrumbs = zip(breadcrumbs_link, category_name)
            return render(request, "postDetail.html", {'instance':instance,'breadcrumbs':breadcrumbs})

    return render(request,"blog/categories.html",{'post_set':parent.post_set.all(),'sub_categories':parent.children.all()})


""""
# slug
https://cedo.tistory.com/43
https://djangopy.org/how-to/how-to-implement-categories-in-django/#conclusion
https://pjs21s.github.io/category-recursive/
https://docs.djangoproject.com/en/3.1/topics/http/urls/
""""

# class showCategoryLV(ListView):
#     model         = Category
#     template_name = 'blog/categories.html'
    
#     def get_queryset(self):
#         return Category.objects.filter(owner=self.request.user)



class PostChangeLV(LoginRequiredMixin,ListView):
    model         = Post
    template_name = 'blog/post_change_list.html'
    
    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)


class PostkUpdateView(OwnerOnlyMixin,UpdateView):
    model       = Post
    fields      = ['title','slug','description','content','tags']
    success_url = reverse_lazy('blog:index') # redirect
    # template_name = 'blog/post_form.html'

class PostDeleteView(OwnerOnlyMixin, DeleteView):
    model         = Post
    success_url   = reverse_lazy('blog:index') # redirect
    template_name = 'blog/post_confirm_delete.html'


class PostYAV(YearArchiveView):
    """
    docstring
    """
    model            = Post
    date_field       = 'modify_dt'
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

https://amamov.tistory.com/107

# on_delete=models.CASCADE 구문이 어떤 동작을 하는지 : https://hashcode.co.kr/questions/1673/%EC%9E%A5%EA%B3%A0-%EA%B5%AC%EB%AC%B8-%EC%A7%88%EB%AC%B8-%EC%9E%85%EB%8B%88%EB%8B%A4

# 이미지 - 참고용 블로그
https://dheldh77.tistory.com/entry/Django-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%97%85%EB%A1%9C%EB%93%9C

# 참고 사이트 ***  
https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Generic_views
# https://velog.io/@mongle/Django-web-project-%EA%B0%9C%EB%B0%9C%EC%9D%BC%EC%A7%806-%ED%8F%AC%ED%86%A0%EC%95%B1-%EA%B8%B0%EB%8A%A5-%EC%B6%94%EA%B0%80

# 객체형 
https://velog.io/@trequartista/TIL14-Django-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EA%B8%B0%EB%8A%A5-%EA%B5%AC%ED%98%84


템플릿 사이트 
https://html5up.net/
https://mdbootstrap.com/freebies/

[참고용] https://all-free-download.com/free-website-templates/

- 섬네일 추가 참고 : https://ldgeao99.tistory.com/120
- 메인 작업시 참고 : https://egg-money.tistory.com/101
"""


