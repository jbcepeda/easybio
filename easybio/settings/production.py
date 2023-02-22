"""
    Configuración para ambiente de Producción
"""
from .base import *
from pathlib import Path
import os
from decouple import config

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =  config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = [config('ALLOWED_HOSTS', 
                       default='')]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE':config('DB_ENGINE'),
            'NAME':config('DB_NAME'),
            'ENFORCE_SCHEMA': config('DB_ENFORCE_SCHEMA', default=True, cast=bool),
            'CLIENT': {
                'host': config('DB_URL')
            }             
        }
}