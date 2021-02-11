from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager  # 태그


# Create your models here.


class LinkList(models.Model):
    """
    제목, url, 내용, 소유자 속성
    추가 - TAG
    """
    title    = models.CharField('TITLE', max_length=100, blank=True)
    url      = models.URLField('URL', unique=True)
    content  = models.TextField('CONTENT', blank=True, help_text='simple text.')
    owner    = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    tags     = TaggableManager(blank=True)

    def __str__(self):
        return self.title
