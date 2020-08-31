"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/"""
import os

#internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#debug = false -> website deployed
#debug = true -> website in development
DEBUG = True

#if debug is false, aws s3 & aws ses settings are activated
if DEBUG == False:
    
    #aws basic settings
    with open('keys/aws_ak.txt') as f:
        AWS_ACCESS_KEY_ID = f.read().strip()
    with open('keys/aws_sk.txt') as f:
        AWS_SECRET_ACCESS_KEY = f.read().strip()
    AWS_STORAGE_BUCKET_NAME = 'sphill67-website'
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = { 'CacheControl': 'max-age=86400',}
    AWS_DEFAULT_ACL = None

    #s3 static settings
    STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static') ]
    AWS_LOCATION = 'static'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

    #s3 public media settings
    DEFAULT_FILE_STORAGE = 'main.storage_backends.MediaStorage'

    #ses/contact form settings
    EMAIL_BACKEND = 'django_ses.SESBackend'
    AWS_SES_REGION_NAME = 'us-east-1'
    AWS_SES_REGION_ENDPOINT = 'email.us-east-1.amazonaws.com'
    AWS_SES_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID
    AWS_SES_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS_KEY

#if debug is true, default django static + media settings & email console are activated 
else:

    #default static settings
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static') ]

    #default media settings
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    #emails via contact form are sent to the console
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#secret key for django project
with open('keys/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

#urls for the website 
ALLOWED_HOSTS = ['*']

#email that gets 400-500 errors
ADMINS = [('admin', 'sphill67.work@gmail.com')]
MANAGERS = [('admin', 'sphill67.work@gmail.com')]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites', 

    #third-party
    'storages',

    #own
    'landing',
    'contact',
]

SITE_ID = 1

#middleware including whitenoise and defaults
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#default root_urlconf
ROOT_URLCONF = 'main.urls'

#default templates with altered dirs
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],

            
    },
}]

#default wsgi
WSGI_APPLICATION = 'main.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
