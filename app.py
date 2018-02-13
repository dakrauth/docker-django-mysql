#!/usr/bin/env python
import os
import sys
from pathlib import Path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app")

BASE_DIR = Path(__file__).parent
ALLOWED_HOSTS = ['*']
DEBUG = True
ROOT_URLCONF = 'app'
SECRET_KEY = 'supersecret'
LANGUAGES = []
STATIC_URL = '/static/'
WSGI_APPLICATION = 'app.application'
INSTALLED_APPS = [
    'django.contrib.admin', 'django.contrib.auth', 'django.contrib.staticfiles',
    'django.contrib.contenttypes', 'django.contrib.sessions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR],
    'APP_DIRS': True,
    'OPTIONS': {'context_processors': [
        'django.contrib.auth.context_processors.auth',
    ]},
}]

DATABASES = {'default': {
    'ENGINE': 'django.db.backends.mysql',
    'PASSWORD': 'root',
    'USER': 'root',
    'NAME': 'ddm',
    'HOST': 'db',
}}


from django.core.wsgi import get_wsgi_application
from django.urls import path
from django.shortcuts import render
from django.contrib import admin

application = get_wsgi_application()
urlpatterns = [
    path('', lambda request: render(request, 'home.html')),
    path('admin/', admin.site.urls),
]


if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
