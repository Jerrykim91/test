<br>

#### portfolio - Test Ver 


<br>

# portfolio - Test Ver 

<br>

## 1. Django 시작하기   
<br>

### 1. 초기 파일 생성  
<br>

프로젝트 파일 > 애플리케이션 

프로젝트 파일 안에 애플리케이션이 들어가는 형태이다. 

```bash
# 프로젝트 생성
$ django-admin startproject 프로젝트이름

# 애플리케이션 생성
$ django-admin startapp 앱 이름 
```

파일을 생성하고 나면 변경사항을 적용해야한다. 

<br>

### 마이그레이션  

```bash
# 마리그레이션을 할때 에러는 없는지 확인한다. 
$ python manage.py check
# 모델의 변경 사항을 기반으로 새 마이그레이션을 생성
$ python manage.py makemigrations 
# 디비에 반영하기 
$ python manage.py migrate
```

<br>

**가장 중요)  `makemigrations`,`migrate`은 모델을 변경할때마다 작업해주어야 한다.** <br>
만일 작업하지 않는다면.  아래와 같은 에러 메세지를 확인 할 수 있다. 
<br>

```bash
# 기존 작업중 모델에 유저를 추가하고 모델을 디비에 반영 안 했을때 나타난 메세지중 하나이다. 
sqlite3.OperationalError: no such column: blog_posts.owner_id
```
항상 에러가 발생 한다면 무슨 에러인지 유심히 보도록 하자 ! => `sqlite3.OperationalError` 

<br>

### 이제 해야할일은 다했니 실행 해보도록하자!
<br>

```bash              
# 런서버
$ python manage.py runserver
```

<br><br>

## 2. 기본 구조 

<br>

### 1. 프로젝트 기본 구성 
<br>

```bash
# 프로젝트 구성 
Django web project
    ㄴ Web01 => 이름을 변경하는것이 공통으로 통제하기 수월함
        ㄴ Web01
            - 프로젝트 설계를 위한 python 패키지들이 저장    
            ㄴ __init__.py 
                - 디렉토리를 패키지처럼 다루라고 알려주는 파일 
                => 이름이 중복되는것을 피하게 하는 모듈의 모음 
            ㄴ asgi.py
                -

            ㄴ setting.py 
                - 프로젝트의 환경 및 구성을 저장
                - 환경 설정이 어떻게 동작하는지 확인
                - 데이터베이스, 사이트 언어 설정 
            ㄴ urls.py
                - 설정파일 
                    - 현재 Django project 의 URL 선언을 저장 => 사이트의 '목차'
                    - url주소와 장고의 기능을 연결 시켜주는 역활 
                    - 장고의 강력한 기능**
            ㄴ views.py
                - 사용자 설정 -> 생성 
            ㄴ wsgi.py
                - 

        ㄴ manage.py
            - 프로젝트를 관리하는 스크립트 admin.py와 코드를 공유 
```

<br><br>

### 2. 어플리케이션 기본 구성 

<br>

어플리케이션을 다루는 데에는 두가지 방법이 있다. <br>
사람마다 다른데 나는 1번 방식을 쓰다가 2번 방식으로 변경 하였다. <br>
<br>

좀더 직관적이고 접근하기 수월하기 때문에 2번 방식으로 작업 방식을 변경하였다. <br>
이 테스트 사이트는 1번 방식으로 작업이 진행 되어있다. <br>
어느것도 나쁘지 않다. 당신이 편하다면 1번이든  2번이든 중요하지 않다. 

<br>

### 1번 방식 
<br>

```bash
# 어플리케이션 구성
Django web project 
어플리케이션이름 => 변경 가능 
        ㄴ어플리케이션이름(127.0.0.1:8000)
                ㄴ  __init__.py 
                ㄴ asgi.py
                ㄴ setting.py
                ㄴ urls.py
                ㄴ views.py
                ㄴ wsgi.py
        ㄴ manage.py
        ㄴ Member(앱1)
                ㄴ # 구성은 프로젝트와 유사 
                ㄴ  __init__.py 
                ㄴ admin.py (어드민 뷰)
                ㄴ apps.py
                ㄴ models.py (모델)
                ㄴ test.py (모델)
                ㄴ views.py (함수형 뷰 & 클래스형 뷰 & 제네릭 뷰)
                ㄴ urls.py  
                    - 사용자 생성 -> 생성하는 것이 더욱 직관적이다. 
                
        ㄴ Static (CSS, js 등 )
            - css, js 같은 파일을 보관한다. 
                ㄴ CSS
                ㄴ js
                ㄴ sass
                ㄴ fonts

        ㄴ Templates(HTML)
                ㄴ member(앱1)
                    ㄴ index.html (member의 index)
                ㄴ (앱2)
                ㄴ (앱3)

        ㄴ Board(앱2)
                ㄴ # 구성은 member(앱1)와 동일 
                # 만약 추가 된다면. 아래의 항목들등이 추가 될 수 있음.. 
                ㄴ fields.py  
                ㄴ forms.py
        ㄴ Blog (앱3)
        ㄴ Poll (앱4)
```
<br>


### 2번 방식 

<br>

이 방식은 어플리케이션 파일안에 `Templates`, `Static` 파일이 들어있다. 

<br>

```bash
# 어플리케이션 구성
Django web project 
어플리케이션이름 => 변경 가능 
        ㄴ어플리케이션이름(127.0.0.1:8000)
                ㄴ  __init__.py 
                ㄴ asgi.py
                ㄴ setting.py
                ㄴ urls.py
                ㄴ views.py
                ㄴ wsgi.py
        ㄴ manage.py
        ㄴ Member(앱1)
                ㄴ # 구성은 프로젝트와 유사 
                ㄴ  __init__.py 
                ㄴ admin.py (어드민 뷰)
                ㄴ apps.py
                ㄴ models.py (모델)
                ㄴ test.py (모델)
                ㄴ views.py (함수형 뷰 & 클래스형 뷰 & 제네릭 뷰)
                ㄴ urls.py  
                    - 사용자 생성 -> 생성하는 것이 더욱 직관적이다. 
                # 추가
                ㄴ Static (CSS, js 등 )
                - css, js 같은 파일을 보관한다. 
                        ㄴ CSS
                        ㄴ js
                        ㄴ sass
                        ㄴ fonts

                ㄴ Templates(HTML)
                        ㄴ member(앱1)
                        ㄴ index.html (member의 index)

        ㄴ Board(앱2)
                ㄴ # 구성은 member(앱1)와 동일 
                # 만약 추가 된다면. 아래의 항목들등이 추가 될 수 있음.. 
                ㄴ fields.py  
                ㄴ forms.py
                # 추가
                ㄴ Static (CSS, js 등 )
                - css, js 같은 파일을 보관한다. 
                ㄴ Templates(HTML)
                        ㄴ Board(앱2)
                        ㄴ index.html (Board index)
        ㄴ Blog (앱3)
        ㄴ Poll (앱4)
```

<br>

어플리케이션을 추가는  <br>
위에서 언급 했다 싶이 `$ django-admin startapp 앱 이름 `을   <br>
터미널에 입력하면 된다. 여기서 주의 할점음 입력하기 전에는 <br>
항상 프로젝트 내부인지를 확인하고 올바른 위치에 설치 하기바란다. 

<br><br>

## 3. 

<br>

```py

```

<br><br>



## 4.

<br>

```py

```

<br><br>





<br>

---

<br>

## Reference <br>

- name &nbsp; : &nbsp;<https://> <br>

<br>
<br>

## Practice makes perfect! <br>

- [내용](주소)