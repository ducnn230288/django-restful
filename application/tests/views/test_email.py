import pytest
from django.core import mail
from rest_framework import status

from application.tests.common_method import login, mail_confirm


@pytest.fixture
def send_invite_user_mail_url():
    return "/api/users/send_invite_user_mail"


@pytest.mark.django_db()
def test_management_user_can_send_invite_user_email(
    client, login_management, send_invite_user_mail_url, email_data
):
    """Test that invitation emails can be sent successfully as an administrator user"""
    login(client, login_management)
    response = client.post(
        send_invite_user_mail_url, email_data, format="json"
    )
    assert response.status_code == status.HTTP_200_OK
    mail_confirm(mail.outbox, email_data["email"], "Welcome")


@pytest.mark.django_db()
def test_general_user_cannot_send_invite_user_email(
    client, login_general, send_invite_user_mail_url, email_data
):
    """Tested that invitation emails cannot be sent normally as a general user."""
    login(client, login_general)
    response = client.post(
        send_invite_user_mail_url, email_data, format="json"
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db()
def test_part_time_user_cannot_send_invite_user_email(
    client, login_part_time, send_invite_user_mail_url, email_data
):
    """Testing that invitation emails cannot be sent as a part-time user"""
    login(client, login_part_time)
    response = client.post(
        send_invite_user_mail_url, email_data, format="json"
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
