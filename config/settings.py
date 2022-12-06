import os
from pathlib import Path

import environ
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

DEVELOPMENT_SECRET_KEY = 'django-insecure-xw@_st411n)*@0bu+eia2i*j6o6+n0tk2u3fnf4^idzo^3f4(f'

# Initialise environment variables
env = environ.Env(
    DJANGO_SECRET_KEY=(str, DEVELOPMENT_SECRET_KEY),
    DJANGO_DEBUG=(bool, False),
    DJANGO_SITE_ID=(int, 1),
    DJANGO_STATIC_DOMAIN=(str, None),
    DB_USERNAME=(str, None),
    DB_PASSWORD=(str, None),
    DB_DATABASE=(str, None),
    DB_HOST=(str, None),
    DB_PORT=(str, None),
    USE_S3=(bool, False),
    EMAIL_HOST=(str, None),
    EMAIL_PORT=(int, None),
    EMAIL_HOST_USER=(str, None),
    EMAIL_HOST_PASSWORD=(str, None),
    EMAIL_USE_TLS=(bool, False),
    EMAIL_USE_SSL=(bool, False),
)
environ.Env.read_env()

SECRET_KEY = env('DJANGO_SECRET_KEY')
DEBUG = env('DJANGO_DEBUG', cast=bool)

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = []

SITE_ID = env('DJANGO_SITE_ID', cast=int)

STATIC_DOMAIN = env('DJANGO_STATIC_DOMAIN')

# Application definition

INSTALLED_APPS = [
    # django built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # concerned 3rd party
    'rosetta',
    'jalali_date',
    'debug_toolbar',
    'phonenumber_field',
    'django_render_partial',
    'tinymce',
    'admin_ordering',
    'storages',
    'sorl.thumbnail',

    # local apps

]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database configuration

DB_USERNAME = env('DB_USERNAME')
DB_PASSWORD = env('DB_PASSWORD')
DB_DATABASE = env('DB_DATABASE')
DB_HOST = env('DB_HOST')
DB_PORT = env('DB_PORT')
DB_IS_AVAIL = all((
    DB_USERNAME,
    DB_PASSWORD,
    DB_DATABASE,
    DB_HOST,
    DB_PORT,
))

if DB_IS_AVAIL:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': DB_DATABASE,
            'USER': DB_USERNAME,
            'PASSWORD': DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation

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

# Jalali date configuration

JALALI_DATE_DEFAULTS = {
    'Strftime': {
        'date': '%Y/%m/%d',
        'datetime': '%H:%M - %Y/%m/%d',
    },
    'Static': {
        'js': [
            # loading datepicker
            'admin/js/django_jalali.min.js',
        ],
        'css': {
            'all': [
                'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}

# Tinymce configuration

TINYMCE_DEFAULT_CONFIG = {
    "height": 800,
    "width": '100%',
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
               "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
               "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
               "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
               "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
               "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
    'font_formats': "Andale Mono=andale mono,times;" +
                    "Arial=arial,helvetica,sans-serif;" +
                    "Arial Black=arial black,avant garde;" +
                    "Book Antiqua=book antiqua,palatino;" +
                    "Comic Sans MS=comic sans ms,sans-serif;" +
                    "Courier New=courier new,courier;" +
                    "Georgia=georgia,palatino;" +
                    "Helvetica=helvetica;" +
                    "Impact=impact,chicago;" +
                    "Symbol=symbol;" +
                    "Tahoma=tahoma,arial,helvetica,sans-serif;" +
                    "Terminal=terminal,monaco;" +
                    "Times New Roman=times new roman,times;" +
                    "Trebuchet MS=trebuchet ms,geneva;" +
                    "Verdana=verdana,geneva;" +
                    'Vazir=Vazir,sans-serif;' +
                    "Webdings=webdings;" +
                    "Wingdings=wingdings,zapf dingbats",
    'content_style': f"@import url('https://{STATIC_DOMAIN}/static/fonts/vazir/vazir.css');" +
                     "h1,h2,h3,h4,h5,h6,p,div{font-family: 'Vazir', sans-serif;}",
}

# Internationalization

LANGUAGE_CODE = 'fa'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True

LANGUAGES = (
    ('fa', _('Persian')),
    ('en', _('English')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

# Static files (CSS, JavaScript, Images)

AWS_STATIC_LOCATION = 'static'
AWS_PUBLIC_MEDIA_LOCATION = 'media'
AWS_PRIVATE_MEDIA_LOCATION = 'media/private'

if env('USE_S3', cast=bool) == '1':
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
    S3_ENDPOINT_URL = env('AWS_S3_ENDPOINT_URL')
    AWS_S3_ENDPOINT_URL = f'https://{S3_ENDPOINT_URL}'
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_CUSTOM_DOMAIN = env('AWS_CUSTOM_DOMAIN')
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    # static files configuration
    STATICFILES_STORAGE = 'config.storage.s3.StaticStorage'
    STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.{S3_ENDPOINT_URL}/{AWS_STATIC_LOCATION}/'

    # public media files configuration
    DEFAULT_FILE_STORAGE = 'config.storage.s3.PublicMediaStorage'

    # private media files configuration
    PRIVATE_FILE_STORAGE = 'config.storage.s3.PrivateMediaStorage'
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static')

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets')
]

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Rosetta configuration

ROSETTA_WSGI_AUTO_RELOAD = True
ROSETTA_SHOW_AT_ADMIN_PANEL = True

# Email configuration

EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = env('EMAIL_USE_TLS', cast=bool)
EMAIL_USE_SSL = env('EMAIL_USE_SSL', cast=bool)
EMAIL_IS_AVAIL = all((EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD))

if EMAIL_IS_AVAIL:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
