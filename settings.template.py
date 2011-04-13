DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': '@app_engine@',
        'NAME': '@app_name@',
        'USER': '@app_name@',
        'PASSWORD': '@app_pwd@',
        'HOST': '@db_host@',
        'PORT': '@db_port@',
    }
}

TIME_ZONE = 'America/Recife'
LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = ''
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '2skism1(%wift9bf(uu%ykzqve=cw8dk*$t+zip(xec3l%j=z$'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'es.urls'

AUTH_PROFILE_MODULE = 'twitter.Perfil'

LOGIN_URL = '/entrar/'
LOGOUT_URL = '/sair/'
LOGIN_REDIRECT_URL = '/'

TEMPLATE_DIRS = (
    '@app_dir@/templates'
    'templates',
)

INSTALLED_APPS = (
    'usuarios',
    'twitter',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
