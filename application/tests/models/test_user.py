import pytest
from django.db.utils import DataError, IntegrityError

from application.models import User
from application.tests.factories.user import UserFactory


def get_user(id):
    return User.objects.get(pk=id)


@pytest.mark.django_db
def test_employee_number_length_can_be_8():
    """Maximum length of employee_number is 8 characters"""
    employee_number = "1" * 8
    user = UserFactory(employee_number=employee_number)
    assert get_user(user.id).employee_number == employee_number


@pytest.mark.django_db
def test_employee_number_length_cannot_be_9_or_longer():
    """employee_number cannot be longer than 9 characters"""
    employee_number = "1" * 9
    with pytest.raises(DataError):
        UserFactory(employee_number=employee_number)


@pytest.mark.django_db
def test_employee_number_length_cannot_be_null():
    """employee_number is not null"""
    with pytest.raises(IntegrityError):
        UserFactory(employee_number=None)


@pytest.mark.django_db
def test_employee_number_length_must_be_unique():
    """employee_number must be unique"""
    employee_number = "1" * 8
    UserFactory(employee_number=employee_number)
    with pytest.raises(IntegrityError):
        UserFactory(employee_number=employee_number)


@pytest.mark.django_db
def test_username_length_can_be_150():
    """Maximum username length is 150 characters"""
    username = "a" * 150
    user = UserFactory(username=username)
    assert get_user(user.id).username == username


@pytest.mark.django_db
def test_username_length_cannot_be_151_or_longer():
    """Maximum length of username cannot exceed 151 characters"""
    username = "a" * 151
    with pytest.raises(DataError):
        UserFactory(username=username)


@pytest.mark.django_db
def test_username_cannot_be_null():
    """username cannot be null"""
    with pytest.raises(IntegrityError):
        UserFactory(username=None)


@pytest.mark.django_db
def test_username_must_be_unique():
    """username must be unique"""
    username = "a" * 150
    UserFactory(username=username)
    with pytest.raises(IntegrityError):
        UserFactory(username=username)


@pytest.mark.django_db
def test_email_length_can_be_254():
    """Maximum email length is 254 characters"""
    email = "a" * 245 + "@test.com"
    user = UserFactory(email=email)
    assert get_user(user.id).email == email


@pytest.mark.django_db
def test_email_length_cannot_be_255_or_longer():
    """Maximum email length cannot exceed 255 characters"""
    email = "a" * 246 + "@test.com"
    with pytest.raises(DataError):
        UserFactory(email=email)


@pytest.mark.django_db
def test_email_cannot_be_null():
    """email cannot be null"""
    with pytest.raises(IntegrityError):
        UserFactory(email=None)


@pytest.mark.django_db
def test_email_must_be_unique():
    """email must be unique"""
    email = "a" * 245 + "@test.com"
    UserFactory(email=email)
    with pytest.raises(IntegrityError):
        UserFactory(email=email)


@pytest.mark.django_db
def test_role_can_be_management():
    """Administrator role"""
    role = User.Role.MANAGEMENT
    user = UserFactory(role=role)
    assert get_user(user.id).role == role


@pytest.mark.django_db
def test_role_can_be_general():
    """general role"""
    role = User.Role.GENERAL
    user = UserFactory(role=role)
    assert get_user(user.id).role == role


@pytest.mark.django_db
def test_role_can_be_part_time():
    """part-time role"""
    role = User.Role.PART_TIME
    user = UserFactory(role=role)
    assert get_user(user.id).role == role
