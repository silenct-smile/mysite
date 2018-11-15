#-*-coding:utf-8 -*-
"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@79))i1!6rngbsc$=eq&=lwxp0tlz%h7h_4+i*d0fv^m=g-6kl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
#这些应用被默认启用是为了给常规项目提供方便，默认开启的某些应用需要至少一个数据表，所以，在使用他们之前需要在数据库中创建一些表。请执行以下
# 命令：python manage.py migrate
"""这个 migrate 命令检查 INSTALLED_APPS 设置，为其中的每个应用创建需要的数据表，至于具体会创建什么，这取决于你的 mysite/settings.py 设置文件
和每个应用的数据库迁移文件（我们稍后会介绍这个）。这个命令所执行的每个迁移操作都会在终端中显示出来。如果你感兴趣的话，运行你数据库的命令行工具，
并输入 \dt (PostgreSQL)， SHOW TABLES; (MySQL)， .schema (SQLite)或者 SELECT TABLE_NAME FROM USER_TABLES; (Oracle) 来看看 Django 到底创建
了哪些表
就像之前说的，为了方便大多数项目，我们默认激活了一些应用，但并不是每个人都需要它们。如果你不需要某个或某些应用，你可以在运行 migrate 前毫无顾虑
地从 INSTALLED_APPS 里注释或者删除掉它们。 migrate 命令只会为在 INSTALLED_APPS 里声明了的应用进行数据库迁移
"""
INSTALLED_APPS = [
    'django.contrib.admin',#管理员站点， 你很快就会使用它
    'django.contrib.auth',#认证授权系统
    'django.contrib.contenttypes',#内容类型框架
    'django.contrib.sessions',#会话框架
    'django.contrib.messages',#消息框架
    'django.contrib.staticfiles',#管理静态文件的框架
    'polls',#但是首先得把 polls 应用安装到我们的项目里
    'blog',
    'rest_framework',
    'rest_framework.authtoken' # token 认证
    #'rest_framework_docs',

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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
#GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'youpassword' WITH GRANT OPTION;
"""并且需要在应用的__init__.py文件添加
import pymysql
pymysql.install_as_MySQLdb()
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME':'mysite',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'39.106.144.229',
        'PORT':'3306',
    }
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

"""
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': (
    # 这句话能够使认证生效，否则直接请求就回返回结果
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
 # 这里是支持缓存，用户名密码，token 三个认证
 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
  # 使用token是必须要有下面这句话
 'rest_framework.authentication.TokenAuthentication',
    ),
    'PAGE_SIZE': 10
}
"""
# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'#找到settings对应的python文件，然后把这个en-us改成zh-Hans就课可以设置成中文了

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
#USE_TZ = True
USE_TZ = False
"""在Django的配置文件settings.py中，有两个配置参数是跟时间与时区有关的，分别是TIME_ZONE和USE_TZ
如果USE_TZ设置为True时，Django会使用系统默认设置的时区，即America/Chicago，此时的TIME_ZONE不管有没有设置都不起作用。
如果USE_TZ 设置为False，而TIME_ZONE设置为None，则Django还是会使用默认的America/Chicago时间。若TIME_ZONE设置为其它时区的话，则还要分情况，
如果是Windows系统，则TIME_ZONE设置是没用的，Django会使用本机的时间。如果为其他系统，则使用该时区的时间，入设置USE_TZ = False, 
TIME_ZONE = 'Asia/Shanghai', 则使用上海的UTC时间"""

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
