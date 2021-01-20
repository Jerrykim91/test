from django.db import models
from django.urls import reverse  # 빨간색 책 139page + 검색해보기 # URL 패턴을 만들어 주는 내장함수


from melog.fields import ThumbnailImageField

# Create your models here.


class Album(models.Model):
    """
    docstring
    """

    name = models.CharField(max_length=50)
    description = models.CharField(
        'One Line Description', max_length=100, blank=True)  # 설명

    class Meta:
        """
        메타 데이터 
        """
        ordering = ('name',)

    def __ste__(self):
        """
        docstring
        """
        return self.title

    def get_absolute_url(self):
        """
        docstring
        """
        return reverse('melog:album_detail', args=(self.id,))


class Photo(models.Model):
    """
    docstring
    """
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField('TITLE', max_length=30)
    description = models.TextField('Photo Description', blank=True)
    image = ThumbnailImageField(upload_to='melog/%y/%m')
    upload_dt = models.DateTimeField('Upload Date', auto_now_add=True)

    class Meta:
        """
        docstring
        """
        ordering = ('title',)

    def __str__(self):
        """
        docstring
        """
        return self.title

    def get_absolute_url(self):
        """
        docstring
        """
        return reverse('melog:photo_detail', args=(self.id,))



# 참고 사잍트  https://velog.io/@mongle/Django-web-project-%EA%B0%9C%EB%B0%9C%EC%9D%BC%EC%A7%806-%ED%8F%AC%ED%86%A0%EC%95%B1-%EA%B8%B0%EB%8A%A5-%EC%B6%94%EA%B0%80