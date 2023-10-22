"""Settings for DEV environment"""

from .base import *
from .environment import aws_settings

DEBUG = False
ROOT_URLCONF = "project.urls.base"

INSTALLED_APPS += [
    "django_ses",
    "storages",
]


# Configuring SES
EMAIL_BACKEND = "django_ses.SESBackend"
AWS_DEFAULT_REGION_NAME = aws_settings.AWS_DEFAULT_REGION_NAME
DEFAULT_FROM_EMAIL = aws_settings.DEFAULT_FROM_EMAIL
# Configuring S3
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3StaticStorage"
AWS_STORAGE_BUCKET_NAME = aws_settings.AWS_STORAGE_BUCKET_NAME
