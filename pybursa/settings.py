"""
Django settings for pybursa project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y0s!oamjz-kzh-vrv0^ev97dstwg89my40gz11w&_%t&igior)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'quadratic',
    'students',
    'courses',
    'coaches',
    'feedbacks',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pybursa.urls'

WSGI_APPLICATION = 'pybursa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'), )

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 1025
ADMINS = (('admin', 'admin@admin.com'))

LOGGING = {
    'version':1,
    'loggers':
    {
        'courses':{
            'handlers':['file_courses', 'file_students'],
            'level':'DEBUG',
        },
        'students':{
            'handlers':['file_students'],
            'level':'DEBUG',
        },

    },
   'handlers':{
        'file_courses':{
            'level':'DEBUG',
            'class':'logging.FileHandler',
            'filename':os.path.join(BASE_DIR, 'courses_logger'),
        },
        'file_students':{
            'level':'WARNING',
            'class':'logging.FileHandler',
            'filename':os.path.join(BASE_DIR, 'students_logger'),
        },
   },
}