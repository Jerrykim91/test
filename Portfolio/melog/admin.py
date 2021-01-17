from django.contrib import admin
from melog.models import Melog

# # Register your models here.
@ admin.register(Melog) # 데코레이터
class MelogAdmin(admin.ModelAdmin):
    """
    admin 사이트에서 어떤모습으로 
    보여줄지를 정의하는 클래스
    """
    list_display = ('id', 'title', 'modify_dt') 
    list_filter = ('modify_dt',)
    search_fields = ('title', 'body')
