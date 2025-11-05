import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET', 'change-me-in-prod')
DEBUG = True if os.environ.get('DJANGO_DEBUG','1') == '1' else False
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'esign',
        'django_crontab',
            'widget_tweaks',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
        # 'esign.middleware.Handle404RedirectMiddleware',

]

ROOT_URLCONF = 'esign_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ]},
    },
]

WSGI_APPLICATION = 'esign_project.wsgi.application'


DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

# Database: use MySQL if env vars provided, otherwise sqlite
# DB_ENGINE = os.environ.get('DB_ENGINE','sqlite')
# if DB_ENGINE == 'mysql' or os.environ.get('DB_ENGINE','').lower() == 'mysql':
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': os.environ.get('DB_NAME','esign_db'),
#             'USER': os.environ.get('DB_USER','root'),
#             'PASSWORD': os.environ.get('DB_PASS',''),
#             'HOST': os.environ.get('DB_HOST','127.0.0.1'),
#             'PORT': os.environ.get('DB_PORT','3306'),
#         }
#     }
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings (console backend by default for dev)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'saurabdahiya870@gmail.com'
EMAIL_HOST_PASSWORD = 'ifsc ycjc anvh nzyx'  # Use App Password, not your normal Gmail password
DEFAULT_FROM_EMAIL = 'contact@eazeesign.com'




# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'server17.servercenter.xyz'  # Outgoing server
# EMAIL_PORT = 465                           # SSL port
# EMAIL_USE_SSL = True                       # Must be True for port 465
# EMAIL_HOST_USER = 'contact@eazeesign.com' # Full email address
# EMAIL_HOST_PASSWORD = 'zXevKGHa~A;JJ&RA'         # Exact password you set in cPanel
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER





LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'


SITE_URL = "http://localhost:8000"  # ya aapke production URL
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_TIMEZONE = 'Asia/Kolkata'

from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'send-reminders-daily': {
        'task': 'esign_app.tasks.send_reminders_task',
        'schedule': crontab(hour=9, minute=0),  # daily 9 AM
    },
}