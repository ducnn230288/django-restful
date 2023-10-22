"""Settings for LOCAL environment"""

from .base import *

DEBUG = True

REST_FRAMEWORK.update(
    {"DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema"}
)

SPECTACULAR_SETTINGS = {
    "TITLE": "Project name",
    "DESCRIPTION": "Details",
    "VERSION": "1.0.0",
}

INSTALLED_APPS += [
    "debug_toolbar",
    "drf_spectacular",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "project.urls.local"

# Django email settings
EMAIL_HOST = "mail"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
# Specify SMTP port 1025
EMAIL_PORT = 1025
# Set encryption of text being sent to False
EMAIL_USE_TLS = False

CSRF_TRUSTED_ORIGINS = ["http://localhost", "http://127.0.0.1"]
