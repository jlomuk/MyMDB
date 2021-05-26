from  config.common_settings import *

DEBUG = True
SECRET_KEY = 'sdfkdjfkdjffsdkfjsdflkjfdsl'


DATABASES['default'].update({
    'NAME': 'mymdb',
    'USER': 'mymdb',
    'PASSWORD': 'development',
    'HOST': 'localhost',
    'PORT': '5432',
})

INTERNAL_IPS = [
    '127.0.0.1',
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'default-locmemcache',
        'TIMEOUT': 10   
    }
}

MEDIA_ROOT = BASE_DIR.parent / 'media_root'
