# portfolio - Test Ver 

<br>

## 1차 - 배포(deployment)테스트

##### 실제로는 3번째 테스트 

git 이 있으면 그냥 진행 없으면 설치 작업 진행 

- `git add` , `git add --all` : 추가      
- `git status` : 스테이지 된 파일, 브랜치상태 등의 정보를 보여줌 
- `git commit -m "first commit"` : 커밋 메세지 작성과 동시에 커밋

<br>
<br>

## [PythonAnywhere](www.pythonanywhere.com) 에 가입 

<br>

초보자로 회원가입 -> 3개월동안만 서버를 열어놓는것이 유효     

이후에는 결제해야하는것 같았다.      

그러니 생각해보고 하는것을 추천! 일단은 편해서 .... 이걸로 진행 ! 

<br>

## 네비바에 콘솔(Consoles)창 이동

가입할때 사용한 내 아이디가 주소가 된다. 

가입하면 상단에 네비바에 콘솔(Consoles)창을 확인가능하다 

거기서 기본세팅을 할것이다. 

콘솔창을 띄운후 

<br>

```bash
git clone 주소.git 
```

<br>

입력해주고 레퍼지토리가 잘 받아졌는지 tree를 통해서 확인해 본다. `$ tree 폴더이름`

가상환경을 추가할건데 bash Consoles에서 내 폴더로 이동한 다음 `$ cd 폴더`  

가상환경을 만든다. `$ virtualenv --python=python버.전 가상환경이름`

가상환경을 활성화 시킨다.  `$ source 가상환경이름/bin/activate` or `workon 가상환경이름`

중간중간 패키지 설치하고 `pip install 모듈`

데이터베이스 초기화 `$ python manage.py migrate` -> `(가상환경이름) $ python manage.py createsuperuser`

정적파일 수집( 서버가 찾을 수 있는 장소에 집합 ) `python manage.py collectstatic`

<br>

## 네비바 Web 창 이동 

Add a new web app 클릭한다.

그다음은 manual configuration 클릭한 후 파이썬 버전을 선택한다 (1차 세팅 완료) 

가상환경 경로를 설정해준다. 

<br>

## WSGI 설정 파일(WSGI configuration file) 설정

```py

import os
import sys

path = '/home/아이디/폴더이름'  
# /home/jerrykim91/Portfolio/myenv/bin/python
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = '설정폴더이름(=폴더이름).settings' # 에러발생 

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())

```

<br>

## Static files 설정 

본인의 경로에 맞게 정해서 해주는것이 포인트 !!! 


| URL |	Directory	|
|:----:|:----------------------------------------:|
|`/static/`|`/home/아이디/폴더이름/static`|
|`/templates/`|`/home/아이디/폴더이름/templates`|
<br>

일단 완료 -> 템플릿 설정 없이 성공 

<br>
<br>

---

#### 완료하기 전 에러 

이것 말고 기존에 있는 작업물로 진행하려다 하루를 날렸는데 
장고가 2버전에서 3 버전으로 변경되면서 os을 이용하는 방식에서 
path 모듈이용방식으로 바뀌었다. 
이부분을 재설정해주니까 탬플릿을 찾지못하는 에러가 해결되었고 ... 여기서만 

이 프로젝트 같은경우 가상환경안에서 장고 프로젝트 폴더를 생성하고 한것이라 
기존에 있는 실패?한 프로젝트를 하나씩 엎어가면서 오류를 찾아보고자 한다. 

역시 컴퓨터는 죄가 없다.... 내가 죄지... 모르는죄 크흡.....

