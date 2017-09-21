import os
import sys
import dj_database_url
from corsheaders.defaults import default_headers

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+)3x&+mcs&w^tw&ni1osqj!@a_f1acr8j+l-$7b)84rviz*+rx'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
	'jet.dashboard',
	'jet',

	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.sitemaps',
	'django.contrib.sites',
	# Libs
	# 'sortedm2m',
	# # 'widget_tweaks',
	# 'easy_thumbnails',
	'rest_framework',
	'rest_framework.authtoken',
	# utils libs
	'corsheaders',

	#My apps
	'api.accounts',
	'api.core',
	'api.news',
	'api.meeting',
	'api.common_questions',
	'api.communities',
	'api.timeline',
	'api.documents',
	'api.gallery',
	'api.contact',
]

SITE_ID = 1

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'whitenoise.middleware.WhiteNoiseMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'corsheaders.middleware.CorsPostCsrfMiddleware',
	'corsheaders.middleware.CorsMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]


WSGI_APPLICATION = 'api.wsgi.application'

REST_FRAMEWORK = {
	'EXCEPTION_HANDLER': 'api.core.utils.custom_exception_handler',
	# Use Django's standard `django.contrib.auth` permissions,
	# or allow read-only access for unauthenticated users.
	'DEFAULT_PERMISSION_CLASSES': (
		'rest_framework.permissions.IsAuthenticated',
	),
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.TokenAuthentication',
		'rest_framework.authentication.SessionAuthentication',
		# 'rest_framework.authentication.BasicAuthentication'
	)
}

# Auth
AUTH_USER_MODEL = 'accounts.User'

CORS_ALLOW_HEADERS = default_headers + (
	'charset=utf-8',
)

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_PREFLIGHT_MAX_AGE = 86400
CORS_ALLOW_METHODS = (
	'DELETE',
	'GET',
	'OPTIONS',
	'PATCH',
	'POST',
	'PUT',
)

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'concilia.sqlite3'),
	}
}

# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
ADMIN_MEDIA_PREFIX = '/static/admin/'


# E-mail
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'admin@dnit.gov.br'


# Heroku settings
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

# Thumbnails
THUMBNAIL_ALIASES = {
	'': {
		'timeline_images': {'size': (250, 220), 'crop': True},
		'home_news': {'size': (300, 200), 'crop': True},
		'home_videos': {'size': (470, 290), 'crop': True},
		'galery_detail': {'size': (220, 165), 'crop': True},
	},
}

# YOUTUBE API
YOUTUBE_API_KEY = 'AIzaSyApRzZncaa999A5WClkrCpCAXleNDec4Zc'

# LOGGING CONFIGURATION
# A logging configuration that writes log messages to the console.
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     # Formatting of messages.
#     'formatters': {
#         # Don't need to show the time when logging to console.
#         'console': {
#             'format': '%(levelname)s %(name)s.%(funcName)s (%(lineno)d) %(message)s'
#         }
#     },
#     # The handlers decide what we should do with a logging message - do we email
#     # it, ditch it, or write it to a file?
#     'handlers': {
#         # Writing to console. Use only in dev.
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'console'
#         },
#         # Send logs to /dev/null.
#         'null': {
#             'level': 'DEBUG',
#             'class': 'logging.NullHandler',
#         },
#     },
#     # Loggers decide what is logged.
#     'loggers': {
#         '': {
#             # Default (suitable for dev) is to log to console.
#             'handlers': ['console'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#         'photologue': {
#             # Default (suitable for dev) is to log to console.
#             'handlers': ['console'],
#             'level': 'DEBUG',
#             'propagate': False,
#         },
#         # logging of SQL statements. Default is to ditch them (send them to
#         # null). Note that this logger only works if DEBUG = True.
#         'django.db.backends': {
#             'handlers': ['null'],
#             'level': 'DEBUG',
#             'propagate': False,
#         },
#     }
# }

# Don't display logging messages to console during unit test runs.
# if len(sys.argv) > 1 and sys.argv[1] == 'test':
#     LOGGING['loggers']['']['handlers'] = ['null']
#     LOGGING['loggers']['photologue']['handlers'] = ['null']

# Local Settings
try:
	from .local_settings import *
except ImportError:
	pass
