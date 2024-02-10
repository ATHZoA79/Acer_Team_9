"""
Django settings for acer_team_9 project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from decouple import Config, RepositoryEnv, config
import os
import dj_database_url
import django_heroku
import dotenv

dotenv.load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-4tejy1l*we6ni76v7$-!+mymqql_d*t5)q7t&ouz2d9-gsbbpm"

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get("ENVIRONMENT") == "development":
    DEBUG = True
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
    SECRE_KEY = os.environ.get("SECRET_KEY")
elif os.environ.get("ENVIRONMENT") == "production":
    DEBUG = False
    DATABASES = {
        "default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))
    }
DEBUG = True

ALLOWED_HOSTS = ["*"]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]

ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_ADAPTER = "allauth.account.adapter.DefaultAccountAdapter"

# Application definition
SITE_ID = 5

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "index",
    "main",
    "init_db",
    # django_allauth configurations
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.line",
    "whitenoise.runserver_nostatic",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "acer_team_9.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "acer_team_9.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# DB_DIR = os.path.join(BASE_DIR, "db.sqlite3")
DB_DIR = os.path.join(BASE_DIR, "db.sqlite3")
if os.environ.get("DEBUG"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
    # DB_DIR = os.path.join(BASE_DIR, "db.sqlite3")
else:
    DATABASES = {
        "default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "zh-hant"

TIME_ZONE = "Asia/Taipei"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_ROOT = "/static/"
STATIC_URL = os.path.join(BASE_DIR, "static/")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        "SCOPE": ["profile", "email"],
        "AUTH_PARAMS": {"access_type": "online"},
        "sites": [3],
    },
    "line": {
        "SCOPE": ["profile", "openid", "email"],
        "AUTH_PARAMS": {"access_type": "online"},
        "sites": [4],
    },
}
# LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/scenic"
LOGOUT_REDIRECT_URL = "/"

django_heroku.settings(locals())
