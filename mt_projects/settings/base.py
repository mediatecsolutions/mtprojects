"""
Django settings for mt_online project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf import global_settings
PROJECT_ROOT_DIRECTORY = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
    'crispy_forms',
    'bootstrap3_datetime',
    'tinymce',

    'mt_projects.user_auth',
    'mt_projects.client',
    'mt_projects.note',
    'mt_projects.project',
    'mt_projects.quote',
    'mt_projects.todo',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mt_projects.urls'

WSGI_APPLICATION = 'mt_projects.wsgi.application'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'theme_advanced_fonts' : 'helvetica',
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'no'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

TIME_ZONE = 'Europe/Oslo'

STATIC_ROOT = 'static'
STATIC_URL = '/static/'
COMPRESS_ENABLED = False
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT_DIRECTORY, 'files'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Django compress
COMPRESS_PRECOMPILERS = (
    ('text/less',
     'lessc {infile} {outfile} --include-path=\'.:' +
     PROJECT_ROOT_DIRECTORY + '/files/less/\''),
)

# Templates
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT_DIRECTORY, 'templates'),
)
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

# Trailing slashes
APPEND_SLASH = True

LOGIN_URL = '/login/'
