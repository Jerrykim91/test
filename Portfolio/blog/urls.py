# blog\urls.py

from django.urls import path, re_path
from blog import views 

app_name='blog'

urlpatterns = [
    
    path('',views.PostLV.as_view(), name= 'index'), # /blog/
    path('post/',views.PostLV.as_view(), name= 'post_list'), # /blog/post/
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'), #/blog/post/???
    path('archive/', views.PostAV.as_view(), name='post_archive'), # /blog/archive/
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'), # /blog/archive/2020
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'), # /blog/archive/2020/Dec
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'), # /blog/archive/2020/Dec/28
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'), # /blog/archive/today/
]

# # 로그인 
# urlpatterns = [

#     # 로그인 기능 
#     # path('sign_up', views.sign_up),
#     # path('sign_in', views.sign_in),
#     # path('user_delete', views.user_delete),
#     # path('sign_out', views.sign_out),
# ]


# # blog 
# urlpatterns = [
    
#     # path('main', views.main, name ='main' ), # main
#     path('about', views.about_me, name ='about' ), # about
#     path('blog', views.blog, name ='blog' ), # blog
#     path('post', views.posting, name ='post' ), # post
#     path('test', views.test, name ='test' ), # test

# ]

