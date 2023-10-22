"""Module for environment variable definition"""

from pydantic import BaseSettings


class DjangoSettings(BaseSettings):
    """Class to set Django-related environment variables"""

    SECRET_KEY: str = "secretkey"
    ALLOWED_HOSTS: str = "localhost 127.0.0.1 [::1] back web"
    POSTGRES_NAME: str = "postgres"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: int = 5432
    TRUSTED_ORIGINS: str = "http://localhost http://localhost:9000"
    SLACK_ENDPOINT_URL: str = "http://test"


class AwsSettings(BaseSettings):
    """Class to set AWS related environment variables"""

    ENDPOINT_URL: str = "http://localstack:4566"
    AWS_DEFAULT_REGION_NAME: str = "ap-northeast-1"
    AWS_STORAGE_BUCKET_NAME: str = "localstack"
    SENDER: str = "example.co.jp"
    DEFAULT_FROM_EMAIL: str = "example.co.jp"


django_settings = DjangoSettings()


aws_settings = AwsSettings()
