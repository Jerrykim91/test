"""
Django settings for Portfolio project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$urcygl$fsfn4l)&cj-mwhbes*b0_%&uus$@em=4g0ax@j+wl@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']  


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'disqus',
    'widget_tweaks',
    'fontawesome-free',
    'taggit.apps.TaggitAppConfig',
    'taggit_templatetags2',
    'django.contrib.sites',
    # app
    'blog',
    'linkList.apps.LinklistConfig',
    'photo.apps.PhotoConfig',
    'melog.apps.MelogConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':[os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR , 'db.sqlite3'),
        }

    #     # mysql
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'jerrykim91$default',
    #     'USER': 'jerrykim91',
    #     'PASSWORD': 'wldms7873',
    #     'HOST': 'jerrykim91.mysql.pythonanywhere-services.com',
    #     'OPTIONS': {
    #             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
    #              # 'sql_mode': 'traditional'
    #         },
    # }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

# 만든 모델 명시
# AUTH_USER_MODEL = 'YourAppName.YourClassName'
# AUTH_USER_MODEL = "ToyMain.join"

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        'OPTION': {'user_attributes': ('username', 'name')},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# LANGUAGE_CODE = 'ko'
LANGUAGE_CODE = 'en'
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# STATIC_URL  = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR,'config','static')]


#shkim
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# TAG

MEDIA_URL = '/media/'
MEDIA_ROOT= os.path.join(BASE_DIR, 'media')

TAGGIT_CASE_INSENSITIVE= True
TAGGIT_LIMIT = 50 

# 뎃글
DISQUS_WEBSITE_SHORTNAME = "http-127-0-0-1-8000-yssnmdadoy"
DISQUS_SHORTNAME = "http-127-0-0-1-8000-yssnmdadoy"
DISQUS_MY_DOMAIN = 'http://127.0.0.1:8000/'

# STATIC_URL  = '/static_test/'
# STATICFILES_DIRS = [BASE_DIR / 'static_test']

SITE_ID = 1

# LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
########################################################


# STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# MEDIA_URL = '/files/' # 업로드 할 경로
# MEDIA_ROOT = os.path.join(BASE_DIR, 'files')


# 코맨트 에러 잡기 
# https://chagokx2.tistory.com/82, https://developer-ankiwoong.tistory.com/920