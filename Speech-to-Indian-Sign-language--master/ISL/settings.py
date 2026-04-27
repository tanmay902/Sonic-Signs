import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

SECRET_KEY = 'ecq$v-2-@rm^l(0!7i=(l5!^@1m@7w$+p^w4z8fan#7t$i1(&i'
DEBUG = True
ALLOWED_HOSTS = ['*']
#ALLOWED_HOSTS = ['speech-to-indian-sign-language.vercel.app', 'localhost']



# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'V2SL',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ISL.urls'

APPEND_SLASH = False


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

WSGI_APPLICATION = 'ISL.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True



# Static files (CSS, JavaScript, Images)
# Static files for CSS, JS, images, etc.
STATIC_URL = '/static/'

# Directory for static files, where you will keep CSS, JS, etc.

# Static files settings
STATIC_URL = '/static/'

# The base directory where your static files are stored
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'V2SL/assets'),  # Add the assets directory for static files
]

# Collect static files into a single folder (optional but good for production)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Media files (user-uploaded files like images, videos)
# If you have a separate assets directory, you can define the media settings like this
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'assets')  # Specify the path to your assets directory
