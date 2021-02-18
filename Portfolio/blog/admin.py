from django.contrib import admin
from blog.models import Post
from .models import Category

# Register your models here.

@ admin.register(Post) # 데코레이터
class PostAdmin(admin.ModelAdmin):
    """
    admin 사이트에서 어떤모습으로 
    보여줄지를 정의하는 클래스
    """
    # 보여줄 필드 
    list_display = ('id', 'title', 'owner','modify_dt','tag_list','category')
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    # 자동으로 채워질 필드 설정 
    prepopulated_fields = {'slug':('title',)}

    def get_queryset(self, request):
        """
        docstring
        """
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        """
        docstring
        """
        return ','.join(o.name for o in obj.tags.all())


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','parent')
    prepopulated_fields = {'slug': ('name',)}
    # search_fields = ('name')