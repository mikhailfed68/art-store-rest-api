"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.18.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import json
import socket
import os
from pathlib import Path

import dj_database_url
from rest_framework.reverse import reverse_lazy
from dotenv import load_dotenv

from oscar.defaults import *

load_dotenv('.env.dev')

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = json.loads(os.getenv("DEBUG", "false"))

ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "127.0.0.1 .localhost [::1]",
    ).split(" ")

CSRF_TRUSTED_ORIGINS = os.getenv(
    "CSRF_TRUSTED_ORIGINS",
    "http://127.0.0.1 http://localhost",
    ).split(" ")

CORS_ALLOWED_ORIGINS = os.getenv(
    'CORS_ALLOWED_ORIGINS',
    "http://localhost:3000"
    ).split(" ")

# Setting for django-debug-tool-bar
if DEBUG:
    hostname, aliaslist, ipaddrlist = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [f"{ip[:-1]}1" for ip in ipaddrlist] + ["127.0.0.1"]

# Application definition

INSTALLED_APPS = [
    "corsheaders",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',

    'django.contrib.sites',
    'django.contrib.flatpages',

    'rest_framework',
    'authors.customapi.apps.OscarAPIConfig',

    # core apps
    'custom_apps.oscar.apps.Shop',
    'oscar.apps.analytics.apps.AnalyticsConfig',
    'oscar.apps.checkout.apps.CheckoutConfig',
    'oscar.apps.address.apps.AddressConfig',
    'oscar.apps.shipping.apps.ShippingConfig',
    'custom_apps.catalogue.apps.CatalogueConfig',
    'oscar.apps.catalogue.reviews.apps.CatalogueReviewsConfig',
    'oscar.apps.communication.apps.CommunicationConfig',
    'custom_apps.partner.apps.PartnerConfig',
    'oscar.apps.basket.apps.BasketConfig',
    'oscar.apps.payment.apps.PaymentConfig',
    'oscar.apps.offer.apps.OfferConfig',
    'oscar.apps.order.apps.OrderConfig',
    'oscar.apps.customer.apps.CustomerConfig',
    'oscar.apps.search.apps.SearchConfig',
    'oscar.apps.voucher.apps.VoucherConfig',
    'oscar.apps.wishlists.apps.WishlistsConfig',
    # dashboard apps
    'custom_apps.dashboard.apps.DashboardConfig',
    'oscar.apps.dashboard.reports.apps.ReportsDashboardConfig',
    'oscar.apps.dashboard.users.apps.UsersDashboardConfig',
    'oscar.apps.dashboard.orders.apps.OrdersDashboardConfig',
    'custom_apps.dashboard.catalogue.apps.CatalogueDashboardConfig',
    'oscar.apps.dashboard.offers.apps.OffersDashboardConfig',
    'oscar.apps.dashboard.partners.apps.PartnersDashboardConfig',
    'oscar.apps.dashboard.pages.apps.PagesDashboardConfig',
    'oscar.apps.dashboard.ranges.apps.RangesDashboardConfig',
    'oscar.apps.dashboard.reviews.apps.ReviewsDashboardConfig',
    'oscar.apps.dashboard.vouchers.apps.VouchersDashboardConfig',
    'oscar.apps.dashboard.communications.apps.CommunicationsDashboardConfig',
    'oscar.apps.dashboard.shipping.apps.ShippingDashboardConfig',

    # 3rd-party apps that oscar depends on
    'widget_tweaks',
    'haystack',
    'treebeard',
    'sorl.thumbnail',   # Default thumbnail backend, can be replaced
    'django_tables2',

    # my specific apps
    "django_filters",
    'storages',
    'django_cleanup.apps.CleanupConfig',

    # my own apps
    'authors',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'middleware.HeaderSessionMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # "django.middleware.http.ConditionalGetMiddleware",
    # 'oscarapi.middleware.ApiGatewayMiddleWare',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'middleware.NotFoundMiddleware',
    'middleware.SetUserResponseMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    # 'oscarapi.middleware.ApiBasketMiddleWare',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

WSGI_APPLICATION = 'config.wsgi.application'

LOGIN_URL = '/dashboard/login/'

LOGIN_REDIRECT_URL = "/"

LOGOUT_REDIRECT_URL = "/"

ROOT_URLCONF = 'config.urls'

NOT_FOUND_IGNORE_PATHS = [
    r'/dashboard/login/',
    r'^/api/.*$',
    r'^/media/.*$',
    r'^/static/.*$',
    r'^/__debug__/.*$',
    r'^/openapi/.*$',
    r'^/swagger-ui/.*$',
]

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"], # templates directory of the project
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.communication.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]

# Databases
DATABASE_URL = os.getenv("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=600,
        conn_health_checks=True,
    )
}

DATABASES['default']['ATOMIC_REQUESTS'] = True


# Cache settings

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv('REDIS_URL'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Paths to custom api modules for django-oscar-api
OSCARAPI_OVERRIDE_MODULES = ["authors.customapi"]


# Per-site Oscar settings
# For more information, see https://django-oscar.readthedocs.io/en/stable/ref/settings.html


# Display Oscar settings
OSCAR_SHOP_NAME = 'Art-Vostorg Store'

# OSCAR_HOMEPAGE = reverse_lazy('api-root')

OSCAR_RECENTLY_VIEWED_PRODUCTS = json.loads(os.getenv("OSCAR_RECENTLY_VIEWED_PRODUCTS", '10'))

OSCAR_RECENTLY_VIEWED_COOKIE_LIFETIME = json.loads(os.getenv('OSCAR_RECENTLY_VIEWED_COOKIE_LIFETIME', '86400'))


# Order Oscar settings
OSCARAPI_INITIAL_ORDER_STATUS = 'На рассмотрении'

OSCAR_INITIAL_ORDER_STATUS = 'На рассмотрении'

OSCAR_INITIAL_LINE_STATUS = 'На рассмотрении'

OSCAR_ORDER_STATUS_PIPELINE = {
    'На рассмотрении': ('Обрабатывается',),
    'Обрабатывается': ('Обработан', 'Закрыт',),
    'Закрыт': (),
}

# Checkout Oscar settings
OSCAR_OFFERS_INCL_TAX = True

OSCAR_ALLOW_ANON_CHECKOUT = True

OSCAR_REQUIRED_ADDRESS_FIELDS = [
    'first_name',
    'last_name',
    'line1',
    'line2',
    'country'
]


# Review Oscar settings
OSCAR_ALLOW_ANON_REVIEWS = False


# Basket Oscar settings
OSCAR_BASKET_COOKIE_LIFETIME = json.loads(os.getenv('OSCAR_BASKET_COOKIE_LIFETIME', '3600'))

OSCAR_MAX_BASKET_QUANTITY_THRESHOLD = json.loads(os.getenv('OSCAR_MAX_BASKET_QUANTITY_THRESHOLD', '10'))


# Currency Oscar settings
OSCAR_DEFAULT_CURRENCY = os.getenv('OSCAR_DEFAULT_CURRENCY', 'RUB')


# Misc Oscar settings
OSCAR_CSV_INCLUDE_BOM = True

OSCAR_URL_SCHEMA = 'https'

OSCARAPI_BLOCK_ADMIN_API_ACCESS = True

OSCARAPI_ENABLE_REGISTRATION = False


# Product and Useraddress Oscar settings
OSCARAPI_PRODUCT_FIELDS = [
    "url",
    "id",
    "title",
    "author",
    "attributes",
    "categories",
    "product_class",
    "images",
    "availability",
    "price",
]

OSCARAPI_PRODUCTDETAIL_FIELDS = [
    "url",
    "id",
    "upc",
    "title",
    "author",
    "description",
    "structure",
    "date_created",
    "date_updated",
    "recommended_products",
    "attributes",
    "categories",
    "product_class",
    "images",
    "price",
    "availability",
    "stockrecords",
    "options",
    "children",
]

OSCARAPI_USERADDRESS_FIELDS = [
    "id",
    "url",
    "first_name",
    "last_name",
    "line1",
    "line2",
    "country",
    "state",
    "search_text",
    "phone_number",
    "notes",
    "is_default_for_shipping",
    "is_default_for_billing",
]


# Communication Oscar settings
OSCAR_SEND_REGISTRATION_EMAIL = json.loads(os.getenv('OSCAR_SEND_REGISTRATION_EMAIL', 'false'))

OSCAR_SAVE_SENT_EMAILS_TO_DB = json.loads(os.getenv('OSCAR_SAVE_SENT_EMAILS_TO_DB', 'true'))

OSCAR_FROM_EMAIL = os.getenv('OSCAR_FROM_EMAIL', 'oscar@example.com')


# Setting Email configuration for sending reset or error email
ENABLED_EMAIL = json.loads(os.getenv("ENABLED_EMAIL", "false"))

if ENABLED_EMAIL:
    EMAIL_USE_TLS = json.loads(os.getenv("EMAIL_USE_TLS", "true"))

    EMAIL_HOST = os.getenv("EMAIL_HOST")

    EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")

    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

    EMAIL_PORT = json.loads(os.getenv("EMAIL_PORT", "25"))

    SERVER_EMAIL = os.getenv("SERVER_EMAIL")

    if not DEBUG:
        ADMINS = [tuple(json.loads(os.getenv("ADMINS", "[]")))]

else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
# Yandex S3 API
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
# https://cloud.yandex.com/en/docs/storage/s3/

ENABLED_YANDEX_STORAGE = json.loads(os.getenv("ENABLED_YANDEX_STORAGE", "false"))

if ENABLED_YANDEX_STORAGE:
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")

    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

    AWS_DEFAULT_ACL = "public-read"

    AWS_S3_ENDPOINT_URL = os.getenv("AWS_S3_ENDPOINT_URL")

    AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME")

    YANDEX_OBJECT_STORAGE_BUCKET_NAME = os.getenv("YANDEX_OBJECT_STORAGE_BUCKET_NAME")

    YANDEX_S3_DOMAIN = os.getenv("YANDEX_S3_DOMAIN")

    AWS_S3_CUSTOM_DOMAIN = f"{YANDEX_OBJECT_STORAGE_BUCKET_NAME}{YANDEX_S3_DOMAIN}"

    # S3 static settings
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"

    STATICFILES_STORAGE = "common.storages.StaticYandexCloudStorage"

    # S3 public media settings
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"

    DEFAULT_FILE_STORAGE = "common.storages.MediaYandexCloudStorage"
else:
    NAME_STATIC_DIR = os.getenv("NAME_STATIC_DIR", "static")

    STATIC_ROOT = BASE_DIR / NAME_STATIC_DIR

    STATIC_URL = f"{NAME_STATIC_DIR}/"

    NAME_MEDIA_DIR = os.getenv("NAME_MEDIA_DIR", "media")

    MEDIA_ROOT = BASE_DIR / NAME_MEDIA_DIR

    MEDIA_URL = f"{NAME_MEDIA_DIR}/"


# CSRF_COOKIE_SECURE = json.loads(os.getenv("CSRF_COOKIE_SECURE", "true"))

# SESSION_COOKIE_SECURE = json.loads(os.getenv("SESSION_COOKIE_SECURE", "true"))

# CSRF_COOKIE_HTTPONLY = json.loads(os.getenv("CSRF_COOKIE_HTTPONLY", "true"))

# SESSION_COOKIE_HTTPONLY = json.loads(os.getenv("SESSION_COOKIE_HTTPONLY", "true"))

# SESSION_COOKIE_SAMESITE = os.getenv("SESSION_COOKIE_SAMESITE", "Lax")

# SESSION_ENGINE = os.getenv("SESSION_ENGINE", "django.contrib.sessions.backends.cache")