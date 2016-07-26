"""
Django settings for renren_new project.

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
SECRET_KEY = 'duvh!lv0n5zvof!-)9!0w%)fcmcx0pegzgmp8afg_74^fzo0*^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    "django.core.context_processors.request",
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
    "django.core.context_processors.static",
)
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'rest_framework.authtoken',
    'drf_multiple_model',
    
    'allauth',
    'allauth.account',

    'rest_auth',
    'rest_auth.registration',
    
    'alipay',
    'corsheaders',
    
    'rr_user',
    'rr_manage',
    'business',
    'others',
    'register',
    'community'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'renren_new.urls'

WSGI_APPLICATION = 'renren_new.wsgi.application'

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'renrendb',
        'USER': 'bos',
        'PASSWORD': 'renrenCaiwu321',
        'HOST': '139.196.33.243',
        'PORT': '',

    }
}

AUTH_USER_MODEL="rr_user.User"

# AUTHENTICATION_BACKENDS = ('rr_user.models.RRModelBackend',)
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh_CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = '/var/www/html/photos/' 
MEDIA_URL='/image/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

LOGGING_ALIPAY = '/home/renren/renren_bo/static/alipay.log'
LOGGING_WXIPAY = '/home/renren/renren_bo/static/weixinpay.log'

REST_SESSION_LOGIN = False
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SITE_ID = 1
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_USERNAME_REQUIRED = True

REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
#         'rest_auth.serializers.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DATE_FORMAT': "%Y-%m-%d",
    'DATE_INPUT_FORMATS': ("%Y-%m-%d",),

    'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S",
    'DATETIME_INPUT_FORMATS': ("%Y-%m-%d %H:%M:%S",)
}

import datetime

JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_auth.serializers.jwt_response_payload_handler',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
}
