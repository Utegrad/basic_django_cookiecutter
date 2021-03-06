"""
Django settings for {{ cookiecutter.project_name }} project.

"""

import os
import environ

ROOT_DIR = environ.Path(os.path.abspath(__file__)) - 2 # ({{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}/settings.py - 2 = {{ cookiecutter.project_slug }}/)
env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
    INTERNAL_IPS=(list, []),
)
env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = ROOT_DIR()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = '{{ cookiecutter.project_slug }}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ ROOT_DIR('templates'), ],
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

WSGI_APPLICATION = '{{ cookiecutter.project_slug }}.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': env.db()
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.normpath(os.path.join(BASE_DIR, 'static')),
]
STATIC_ROOT = os.path.normpath(env("STATIC_ROOT"))

MEDIA_URL = '/media/'
MEDIA_ROOT = env("MEDIA_ROOT")

ALLOWED_HOSTS = env("ALLOWED_HOSTS")
DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = env("INTERNAL_IPS")
LANGUAGE_CODE = 'en-us'

TIME_ZONE = '{{ cookiecutter.timezone }}'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOGFILE = os.path.join(BASE_DIR, "{{ cookiecutter.project_slug }}.log")
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'console': {
#             'format': '%(message)s',
#         },
#         "simple": {
#             "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
#         }
#     },
#     'handlers': {
#         "console": {
#             "class": "logging.StreamHandler",
#             "level": "INFO",
#             "formatter": "console",
#         },
#         "rolling_file_handler": {
#             "class": "logging.handlers.RotatingFileHandler",
#             "level": "DEBUG",
#             "formatter": "simple",
#             "filename": LOGFILE,
#             "maxBytes": 102400,
#             "backupCount": 5,
#             "encoding": "utf8"
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', ],
#             'level': 'INFO',
#             'propagate': True,
#         },
#         '{{ cookiecutter.project_slug }}': {
#             'handlers': ['rolling_file_handler', 'console', ],
#             'propagate': False,
#             'level': 'DEBUG',
#         },
#     },
# }

