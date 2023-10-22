import uuid

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    """system user"""

    username_validator = UnicodeUsernameValidator()

    class Role(models.IntegerChoices):
        """System user role

        Args:
            MANAGEMENT(0): manager
            GENERAL(1):    generally
            PART_TIME(2):  part-time job
        """

        MANAGEMENT = 0
        GENERAL = 1
        PART_TIME = 2

    # Unnecessary fields can be set to None
    first_name = None
    last_name = None
    date_joined = None
    groups = None
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_comment="system user ID",
    )
    employee_number = models.CharField(
        unique=True,
        validators=[RegexValidator(r"^[0-9]{8}$")],
        max_length=8,
        db_comment="employee number",
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
        db_comment="User name",
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        db_comment="email address",
    )
    role = models.PositiveIntegerField(
        choices=Role.choices,
        default=Role.PART_TIME,
        db_comment="System user role",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_comment="Created date",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        db_comment="Update date",
    )

    USERNAME_FIELD = "employee_number"
    REQUIRED_FIELDS = ["email", "username"]

    class Meta:
        ordering = ["employee_number"]
        db_table = "User"
        db_table_comment = "system user"

    def __str__(self):
        return self.username
