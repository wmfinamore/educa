from .base import *
from decouple import config


DEBUG = False

ADMINS = (
    ('Willian Moreira Finamore', 'finamore.wm@gmail.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DBNAME'),
        'USER': config('DBUSER'),
        'HOST': config('DBHOST'),
        'PORT': config('DBPORT'),
    }
}
