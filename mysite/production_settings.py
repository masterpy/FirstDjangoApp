# mysite/mysite/production_settings.py

# import all default settings
from .settings import *

import dj_database_url
DATABASE = {
    'default': dj_database_url.config()
}

# static asset configuration
STATIC_ROOT = 'staticfiles'

# Honor the 'X-Forwarded-Proto' header for request.is_secure().
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#Allow all host headers
ALLOWED_HOSTS = ['*']

# Turn off DEBUG mode
DEBUG = false

