from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': 'dbempleado',
        'USER': 'rodrigo',
        'PASSWORD': 'rorro13',
        'HOST': 'localhost',
        'PORT': '5432'
        
        
    }
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

#configurar los archivos estaticos desde la carpeta static
STATICFILES_DIRS=[BASE_DIR.child('static')]  #el dir viene de Base apunta a la carpeta static que esta en raiz


#Para configurar que todos los archivos multimedia esten en la carpeta media.
MEDIA_URL='/media/'
MEDIA_ROOT=BASE_DIR.child('pro_empleados.media')