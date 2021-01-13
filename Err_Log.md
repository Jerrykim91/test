
##  DISQUS
왜 DISQUS 동작을 안하는가? 그대? 왜 나타 나지 않는가?

```PY
# 책 
DISQUS_SHORTNAME = "MY SHORTNAME"
DISQUS_MY_DOMAIN = 'http://127.0.0.1:8000/'
```

책에서 언급한 내용과 달리 동작을 안한다. 그래서 ... 
인터넷을 겁나 뒤져서 
찾았다.

```PY
# setting.py
DISQUS_WEBSITE_SHORTNAME = "MY SHORTNAME"
SITE_ID = 1

# 로드 하고자하는 위치
{% load disqus_tags %}  #s 조심 
<div  id="disqus_thread">
    {% disqus_show_comments %}
</div>
```
위 두가지만 넣으면 동작한다. 만약 동작하지 않는다면 pip install 패키지를 설치 해 보자.
그래도 안된다면 ...  DISQUS_WEBSITE_SHORTNAME를 살리고 아래것들을 주석 다니까 서버가 죽었다... 
ㅎㅎㅎㅎ 
에라이 그냥 다 쓰고말지 이게 왜 되는지 모르겟다는 ... 
```py
DISQUS_WEBSITE_SHORTNAME =  "MY SHORTNAME"
DISQUS_SHORTNAME =  "MY SHORTNAME"
DISQUS_MY_DOMAIN = 'http://127.0.0.1:8000/'
```


## 갑자기 어드민이 죽었을때 

OperationalError at /admin/login/
django.contrib.sites.models.Site.DoesNotExist: Site matching query does not exist.

-> 간단한 해결책 : 
```py
# setting.py

SITE_ID = 1 # 맨 아래에 작성 

```
```py

# https://stackoverflow.com/questions/16068518/django-site-matching-query-does-not-exist


python manage.py shell

>>> from django.contrib.sites.models import Site
>>> site = Site()
>>> site.domain = 'example.com' 
>>> site.name = 'example.com'
>>> site.save()

혹은 

>>> from django.contrib.sites.models import Site
>>> site = Site.objects.create(domain='example.com', name='example.com')
>>> site.save()


```

## static 경로를 못찾을때 

하 아무리해도 뭔가 경로를 못찾는다.
그래서 인터넷을 겁나 뒤졌더니 

{% load static %} 하고 static 에서 불러 올 애들은 
예) ` <link rel="stylesheet" href="{% static 'ass.css' %}" />` 이렇게 하란다. 
젠장 .... 
책에도 나와있었네.... 
성질이 급해서 참 등잔 밑이 어둡네 ... .