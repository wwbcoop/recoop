# ReCoop

import os
from django.utils.translation import ugettext_lazy as _


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.abspath( os.path.dirname(__file__) )

# Assets (CSS, JavaScript, Images)

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'recoop', 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'assets/static')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'assets/media')
MAINTENANCE_IGNORE_URLS = (
    r'^/admin/.*',
    r'^/login$',
)

# Registration

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/logout'
LOGOUT_REDIRECT_URL = '/'

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_OPEN = True

# Document settings
DOCUMENT_TITLE = 'coop.re'
DOCUMENT_DESCRIPTION = _(
    'coop.re es un dominio colectivo para la visibilización '
    'y empoderamiento de la economía cooperativa y las prácticas '
    'que crean bien común'
)

# Sites conf
SITE_ID = 1

# Apps
CONTRIB_APPS = (
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'captcha',
    'ckeditor',
)

PROJECT_APPS = (
    'apps.utils',
    'apps.textblock',
    'apps.feather',
    'apps.contact',
    'apps.initiative',
)

INSTALLED_APPS = CONTRIB_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'recoop.urls'

TEMPLATES = [
    {
        'BACKEND' : 'django.template.backends.django.DjangoTemplates',
        'DIRS' : [ 'recoop/templates' ],
        'APP_DIRS' : True,
        'OPTIONS' : {
            'context_processors' : [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'recoop.context_processors.site_info_processor',
                'recoop.context_processors.debug_processor',
            ],
            'builtins' : [
                'recoop.templatetags.tags'
            ]
        },
    },
]

WSGI_APPLICATION = 'recoop.wsgi.application'

#
# Internationalization
#
LANGUAGE_CODE = 'es'
LANGUAGES = (
    ('en', _('English')),
    ('es', _('Español')),
)
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ   = True
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
DECIMAL_SEPARATOR = '.'

# CKEditor
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL  = "/static/admin/js/vendor/jquery/jquery.min.js"

#
# Import private settings
#
from .private_settings import *
