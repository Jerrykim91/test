from django.contrib import admin
from linkList.models import LinkList

# Register your models here.

@ admin.register(LinkList)
class LinkListAdmin(admin.ModelAdmin):
    list_display =('id', 'title', 'url')
    search_fields = ('title', 'content')