from django.db import models
from django.urls import reverse  # 빨간색 책 139page + 검색해보기 # URL 패턴을 만들어 주는 내장함수

# Create your models here.


class Melog(models.Model):
    """
    docstring
    """
    
    title        = models.CharField(verbose_name='TITLE', max_length = 100)
    create_dt    = models.DateTimeField('CREATE DATE', auto_now_add=True) # 글 작성시간
    modify_dt    = models.DateTimeField('MODIFY DATE', auto_now=True) # 글 수정 시간 
    body         = models.TextField('BODY') 

    class Meta:
        """
        docstring
        """
        verbose_name = 'mepost'
        verbose_name_plural = 'meposts'  # 복수 별칭
        db_table = 'melog_posts'


    def __ste__(self):
        """
        docstring
        """
        return self.title

    # def get_absolute_url(self):
    #     """
    #     docstring
    #     """
    #     return reverse('melog:index', args=(self.id,))

    # def get_previous(self):
    #     """
    #     get_previous_by_modify_dt: 장고의 내장함수로 modify_dt()를 기준으로 최신포스트를 반환
    #     """
    #     return self.get_previous_by_modify_dt()
    
    # def get_next(self):
    #     """
    #     # get_next_by_필드명()은 Django의 내장함수
    #     """
    #     return self.get_next_by_modify_dt()