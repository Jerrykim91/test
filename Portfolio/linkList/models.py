from django.db import models

# Create your models here.

class LinkList(models.Model):
    title = models.CharField('TITLE',max_length=100, blank=True)
    url = models.URLField('URL', unique=True)
    content = models.TextField('CONTENT', blank=True, help_text='simple text.')


    def __str__(self):
        return self.title 