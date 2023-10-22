import pytest

from application.models import User
from application.serializers.user import UserSerializer


@pytest.fixture
def user_data():
    """System user input data"""

    return {
        "employee_number": "1" * 8,
        "username": "test_user_01",
        "email": "test@example.com",
        "role": User.Role.GENERAL,
    }


@pytest.mark.django_db
def test_validate_user_data(user_data):
    """User data does not result in validation error"""
    serializer = UserSerializer(data=user_data)
    assert serializer.is_valid()


@pytest.mark.django_db
def test_employee_number_length_cannot_be_7_or_shorter(user_data):
    """Validation error occurs because employee_number of user is less than 7 characters"""
    user_data["employee_number"] = "1" * 7
    serializer = UserSerializer(data=user_data)
    assert not serializer.is_valid()
