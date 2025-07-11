"""
Django settings for rustdesk_server_api project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
if "CSRF_TRUSTED_ORIGINS" in os.environ:
    CSRF_TRUSTED_ORIGINS = [os.environ["CSRF_TRUSTED_ORIGINS"]]
else:
    CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:21114"]
    SECURE_CROSS_ORIGIN_OPENER_POLICY = 'None'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", 'dSKXd*XYWLHCKTQS*4lV6$fmDzBX1%T18T^6OrGoksY@idapP4k9rux0J*v4VNCm')
# ID server IP or domain name, usually with relay server, used for web client
ID_SERVER = os.environ.get("ID_SERVER", '')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", False)
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
ALLOWED_HOSTS = ["*"]
AUTH_USER_MODEL = 'api.UserProfile'      # AppName.自定义user (AppName.Custom user)

ALLOW_REGISTRATION = os.environ.get("ALLOW_REGISTRATION", "False")         # Whether to allow registration, True means allowed, False means not allowed
ALLOW_REGISTRATION = True if ALLOW_REGISTRATION.lower() == 'true' else False

GHUSER = os.environ.get("GHUSER", '')
GHBEARER = os.environ.get("GHBEARER", '')
GENURL = os.environ.get("GENURL", '')
PROTOCOL = os.environ.get("PROTOCOL", 'https')
REPONAME = os.environ.get("REPONAME", 'rustdesk-api-server')

USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True

# ==========数据库配置 开始=====================
DATABASE_TYPE = os.environ.get("DATABASE_TYPE", 'SQLITE')
MYSQL_DBNAME = os.environ.get("MYSQL_DBNAME", '-')
MYSQL_HOST = os.environ.get("MYSQL_HOST", '127.0.0.1')
MYSQL_USER = os.environ.get("MYSQL_USER", '-')
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", '-')
MYSQL_PORT = os.environ.get("MYSQL_PORT", '3306')
# ==========数据库配置 结束=====================

LANGUAGE_CODE = os.environ.get("LANGUAGE_CODE", 'en')
# #LANGUAGE_CODE = os.environ.get("LANGUAGE_CODE", 'en')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'webui',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',   # 取消post的验证。
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rustdesk_server_api.urls'

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
                'api.util.settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'rustdesk_server_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db/db.sqlite3',
    },
}
if DATABASE_TYPE == 'MYSQL' and MYSQL_DBNAME != '-' and MYSQL_USER != '-' and MYSQL_PASSWORD != '-':
    # 简单通过数据库名、账密信息过滤下，防止用户未配置mysql却使用mysql
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': MYSQL_DBNAME,               # 数据库名
            'HOST': MYSQL_HOST,                 # 数据库服务器IP
            'USER': MYSQL_USER,                 # 数据库用户名
            'PASSWORD': MYSQL_PASSWORD,         # 数据库密码
            'PORT': MYSQL_PORT,                 # 端口
            'OPTIONS': {'charset': 'utf8'},
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Australia/Melbourne'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = 'static/'

if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')     # 新增

LANGUAGES = (
    ('zh-hans', '中文简体'),
    ('en', 'English'),

)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
