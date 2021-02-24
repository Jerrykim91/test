from django.contrib import admin
from blog.models import Post
from .models import Category, PhotoArt

# 마크다운
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
class PhotoInline(admin.TabularInline):
    model = PhotoArt

@ admin.register(Post) # 데코레이터
class PostAdmin(MarkdownxModelAdmin):
    """
    admin 사이트에서 어떤모습으로 
    보여줄지를 정의하는 클래스
    """
    # 보여줄 필드 
    list_display = ('id', 'title', 'owner','modify_dt','tag_list','category')
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    inlines = [PhotoInline, ] # Post 클래스는 해당하는 Photo 객체를 리스트로 관리하는 한다. 

    # 자동으로 채워질 필드 설정 
    prepopulated_fields = {'slug':('title',)}

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ','.join(o.name for o in obj.tags.all())



# Category
admin.site.register(Category)

# PhotoArt
admin.site.register(PhotoArt)

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'parent')
#     prepopulated_fields = {'slug': ('name',)}
#     # search_fields = ('name')


# Photo 클래스를 inline으로 나타낸다.



# Register your models here.
# admin.site.register(Post, PostAdmin)