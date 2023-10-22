import json
from enum import Enum
from logging import getLogger

import requests
from django.utils.log import AdminEmailHandler

from project.settings.environment import django_settings


class LoggerName(Enum):
    """Logger name"""

    APPLICATION = "application"
    EMERGENCY = "emergency"


class SlackHandler(AdminEmailHandler):
    def send_mail(self, subject, message, *args, **kwargs):
        webhook_url = django_settings.SLACK_ENDPOINT_URL
        if "Request" in message:
            alarm_emoji = ":rotating_light:"
            text = alarm_emoji + message.split("COOKIES")[0]
            data = json.dumps(
                {
                    "attachments": [{"color": "#e01d5a", "text": text}],
                }
            )
            headers = {"Content-Type": "application/json"}
            getLogger(LoggerName.EMERGENCY.value).error(message)
            requests.post(url=webhook_url, data=data, headers=headers)
