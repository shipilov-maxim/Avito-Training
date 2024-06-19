import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

dot_env = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=dot_env)

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
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

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'HOST': os.environ.get('POSTGRES_HOST'),
    #     'NAME': os.environ.get('POSTGRES_DB'),
    #     'USER': os.environ.get('POSTGRES_USER'),
    #     'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
    #     'PORT': os.environ.get('POSTGRES_PORT'),
    #
    # },
    'default': {
        "ENGINE": "djongo",
        "NAME": os.environ.get('MONGO_DB_NAME'),
        'ENFORCE_SCHEMA': False,
        "CLIENT": {
            "host": os.environ.get('MONGO_DB_HOST'),
            "port": int(os.environ.get('MONGO_DB_PORT')),
            # "username": os.environ.get('MONGO_DB_USERNAME'),
            # "password": os.environ.get('MONGO_DB_PASSWORD'),
        },
        # 'TEST': {
        #     'MIRROR': 'default',
        # },
    }
}

# DATABASE_ROUTERS = ['app.utils.db_routers.NonRelRouter', ]

CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_IGNORE_RESULT = True
CELERY_BROKER_URL = os.environ.get('CELERY_URL')
CELERYD_HIJACK_ROOT_LOGGER = False
REDIS_CHANNEL_URL = os.environ.get('REDIS_CHANNEL_URL')

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

ENCRYPT_KEY = b'tmzHcYuvLUhxjcxZ4k_iqfCx-HUq6PCvdbXr4vOC5B4='

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Samara'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
