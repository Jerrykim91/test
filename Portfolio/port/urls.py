# # blog\urls.py

# from django.urls import path, re_path
# from port import views
# from django.views.generic import TemplateView

# app_name = 'port'

# urlpatterns = [

#     # MELOG
#     # path('', TemplateView.as_view(template_name = 'blog/post_about_me.html')),  # /melog/
#     path('', views.indexView.as_view(), name='index'),  # /melog/

#     ##################################################

#     # path('',views.PostLV.as_view(), name='index'), # /blog/
#     # path('post/',views.PostLV.as_view(), name='post_list'), # /blog/post/
#     # re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'), #/blog/post/???
#     # path('archive/', views.PostAV.as_view(), name='post_archive'), # /blog/archive/
#     # path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'), # /blog/archive/2020
#     # path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'), # /blog/archive/2020/Dec
#     # path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'), # /blog/archive/2020/Dec/28
#     # path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'), # /blog/archive/today/

#     # # TAG
#     # path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'), # /blog/tag/
#     # path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'), # /blog/tag/tagname/

#     # # Search
#     # path('search/', views.SearchFormView.as_view(), name='search'),

# ]