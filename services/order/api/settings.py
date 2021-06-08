"""
Django settings for Order_service project.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e7651386-8152-40cb-8a72-b5d14f34b139'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application references
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'corsheaders',
    'rest_framework',
    'django_extensions'
]

# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'api.urls'

# Template configuration
# https://docs.djangoproject.com/en/2.1/topics/templates/
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

WSGI_APPLICATION = 'api.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# TODO – Move all creads to .env file
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', default="ec2-54-220-53-223.eu-west-1.compute.amazonaws.com")
POSTGRES_DB = os.environ.get('POSTGRES_DB', default="d2j9sc39u03m7")
POSTGRES_USER = os.environ.get('POSTGRES_USER', default="srxcrdmbedglpr")
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD',
                                   default="f60781f913431d429418b8cce31cdac7c8222b8385f9c05d34fcba3389488f4e")

print(f'POSTGRES_HOST: {POSTGRES_HOST}\n'
      f'POSTGRES_DB: {POSTGRES_DB}\n',
      f'POSTGRES_USER: {POSTGRES_USER}\n'
      f'POSTGRES_PASSWORD: {POSTGRES_PASSWORD}\n')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': POSTGRES_DB,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': POSTGRES_HOST,
        'PORT': 5432,
    }
}

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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

CORS_ORIGIN_ALLOW_ALL = True  # If this is used then `CORS_ORIGIN_WHITELIST` will not have any effect
CORS_ALLOW_CREDENTIALS = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
