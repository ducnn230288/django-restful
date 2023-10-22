"""AWS related modules"""
from logging import Logger, getLogger

from botocore.client import BaseClient
from botocore.exceptions import ClientError
from injector import inject

from application.utils.logs import LoggerName

application_logger: Logger = getLogger(LoggerName.APPLICATION.value)
emergency_logger: Logger = getLogger(LoggerName.EMERGENCY.value)


# https://docs.aws.amazon.com/ses/latest/dg/example_ses_SendEmail_section.html
class SesResource:
    """Class for Ses Resource"""

    def __init__(self, ses_client: BaseClient):
        self.ses_client = ses_client


class SesWrapper:
    """Encapsulates Amazon SES topic and subscription functions."""

    @inject
    def __init__(self, ses_client: SesResource):
        """
        :param sns_resource: A Boto3 Amazon SNS resource.
        """
        self.ses_client = ses_client

    def send_email(
        self,
        source: str,
        to_addresses: str,
        subject: str,
        body_text: str,
        charset: str,
    ) -> None:
        """AWS Send email using SES

        Args:
            source (str): sender
            to_addresses (str): mail recipient
            subject (str): email subject
            body_text (str): Email body
            charset(str): Character code
        """
        try:
            response = self.ses_client.send_email(
                Destination={
                    "ToAddresses": [
                        to_addresses,
                    ],
                },
                Message={
                    "Body": {
                        "Text": {
                            "Charset": charset,
                            "Data": body_text,
                        },
                    },
                    "Subject": {
                        "Charset": charset,
                        "Data": subject,
                    },
                },
                Source=source,
            )
        except ClientError as error:
            message = error.response["Error"]["Message"]
            emergency_logger.exception(message)
        else:
            message = "Email sent! Message ID:", response["MessageId"]
            emergency_logger.exception(message)
