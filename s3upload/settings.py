from os import environ as CONFIG

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = tuple(admin.split(':') for admin in CONFIG.get('DJANGO_ADMINS', '').split(',') if admin != '')
MANAGERS = ADMINS
DATABASES = {
    'default': {}
}
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = False
SECRET_KEY = CONFIG['DJANGO_SECRET']
TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',)
MIDDLEWARE_CLASSES = ()
ROOT_URLCONF = 's3upload.urls'
WSGI_APPLICATION = 's3upload.wsgi.application'
TEMPLATE_DIRS = (CONFIG['PROJECT_ROOT'] + '/s3upload/templates',)
STATIC_ROOT=CONFIG['PROJECT_ROOT'] + '/s3upload/static'
INSTALLED_APPS = (
)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {},
    'loggers': {}
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
AWS_ACCESS_KEY_ID = CONFIG['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = CONFIG['AWS_SECRET_ACCESS_KEY']
AWS_S3_BUCKET_URL = CONFIG['AWS_S3_BUCKET_URL']
AWS_S3_BUCKET_NAME = AWS_S3_BUCKET_URL.split('.')[0].split('//')[1]
