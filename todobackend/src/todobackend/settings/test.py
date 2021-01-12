from todobackend.settings.base import *
import os

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

INSTALLED_APPS += ('django_nose',)
TEST_RUNNER = 'django.nsoe.NoseTestSuiteRunner'
TEST_OUTPUT_DIR = os.environ.get('TEST_OUTPUT_DIR', '.')

NOSE_ARGS = ['--verbosity=2', 
             '--nologcapture',
             '--with-coverage',
             '--cover-package=todo',
             '--with-spec',
             '--spec-color',
             '--with-xunit',
             '--cover-xml',
             ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE','todobackend'),
        'USER': os.environ.get('MYSQL_USER','todo'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD','password'),
        'HOST': os.environ.get('MYSQL_HOST','localhost'),
        'PORT': os.environ.get('MYSQL_PORT','3306'),
    }
}