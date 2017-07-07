from .base import *

DEBUG=False

ADMINS=(
    ('H Marjak','hmarjak@interia.pl'),
)

ALLOWED_HOSTS=['hmarjak.pythonanywhere.com','www.hmarjak.pythonanywhere.com']

DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}