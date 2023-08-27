from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-!*nvojxa_676pi1g@z1zb*&y=m1p$@5d=lp@bp&)@psyqk-zl9'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'rest_framework',
    'posts'
]

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        'rest_framework.renderers.JSONRenderer',
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": [],
    "UNAUTHENTICATED_USER": None,
}

ROOT_URLCONF = 'service.urls'

WSGI_APPLICATION = 'service.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
