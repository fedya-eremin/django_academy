"""
Django settings for myserver project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

env = environ.Env(
    SECRET_KEY=(str, "default"),
    DEBUG=(bool, True),
    DATABASE_NAME=(str, "db.sqlite3"),
    ALLOWED_HOSTS=(list, ["localhost"]),
    DATABASE_USER=(str, None),
    DATABASE_PASS=(str, None),
    INTERNAL_IPS=(list, ["127.0.0.1"]),
    ENABLE_REVERSE_RU_MIDDLEWARE=(bool, False),
    VALIDATE_WORDS=(list, ["роскошно", "превосходно"]),
    DEFAULT_FROM_EMAIL=(str, "example@ya.ru"),
    NEW_USER_ACTIVATED=(bool, False),
)
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")
VALIDATE_WORDS = env("VALIDATE_WORDS")
NEW_USER_ACTIVATED = env("NEW_USER_ACTIVATED")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")
if DEBUG is True:
    ALLOWED_HOSTS = ["*"]
    NEW_USER_ACTIVATED = True
else:
    ALLOWED_HOSTS = env("ALLOWED_HOSTS")


# Application definition

INSTALLED_APPS = [
    "homepage.apps.HomepageConfig",
    "catalog.apps.CatalogConfig",
    "about.apps.AboutConfig",
    "feedback.apps.FeedbackConfig",
    "users.apps.UsersConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",
    "sorl.thumbnail",  # Thumbnails, mostly for admin panel
    "django_cleanup.apps.CleanupConfig",  # To work with images
    "compressor",  # Adds CSS, SASS, JS compressor and so on
    "django_quill",  # Text processor in admin panel
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

if env("ENABLE_REVERSE_RU_MIDDLEWARE") is True:
    MIDDLEWARE.append("myserver.middleware.ReverseRuMiddleware")

INTERNAL_IPS = env("INTERNAL_IPS")

ROOT_URLCONF = "myserver.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "myserver.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASS"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation"
            ".UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.NumericPasswordValidator"
        ),
    },
]


LOGIN_URL = "/auth/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/auth/logout/"


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ("ru", "Russian"),
    ("en", "English"),
)

LOCALE_PATHS = (BASE_DIR / "locale",)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static_dev",
]
# Following lines are adding SASS to project
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]
COMPRESS_ROOT = BASE_DIR / STATICFILES_DIRS[0]
# Following command will be executet if either STATIC_ROOT or
# COMPRESS_PRECOMPILERS is set
COMPRESS_PRECOMPILERS = (("text/x-scss", "django_libsass.SassCompiler"),)

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# configure QuillFields (default config from docs :)
QUILL_CONFIGS = {
    "default": {
        "theme": "snow",
        "modules": {
            "syntax": True,
            "toolbar": [
                [
                    {"font": []},
                    {"header": []},
                    {"align": []},
                    "bold",
                    "italic",
                    "underline",
                    "strike",
                    "blockquote",
                    {"color": []},
                    {"background": []},
                ],
                ["code-block", "link"],
                ["clean"],
            ],
        },
    }
}

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = BASE_DIR / "sent_mails"
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")
