from defaults import *

# Allowed hosts. Add host domain or IP to it. Do not add '*'.
# Example: ['www.example.com']
# https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['127.0.0.1']

# You should generate a new secret key for production.
# Secret key generator: http://www.miniwebtool.com/django-secret-key-generator/
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SECRET_KEY
SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Modify it for any changes on apps, this variable is for Django template loader.
# https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.app_directories.Loader
# INSTALLED_APPS += ('example_app',)
