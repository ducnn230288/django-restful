def login(client, login_authority):
    """Login process
    Args:
        client: APIClient
        login_authority[dict]:Login privileges
    """
    client.login(
        username=login_authority["employee_number"],
        password=login_authority["password"],
    )


def mail_confirm(mail_outbox, sender: str, message: str):
    """Test to check if the email was sent successfully
    Args:
        mail_outbox (List[EmailMessage]): Django test email inbox
        sender (str): Sender of email
        message (str): Email subject
    """
    # Confirm that you have received an email
    assert len(mail_outbox) == 1
    assert mail_outbox[0].subject == message
    assert mail_outbox[0].from_email == "example@mail.com"
    assert mail_outbox[0].to[0] == sender
