import pytest
from rest_framework import status

from application.tests.common_method import login


@pytest.fixture
def get_login_url():
    return "/api/auth/login"


@pytest.fixture
def get_logout_url():
    return "/api/auth/logout"


@pytest.mark.django_db
def test_management_user_can_login(client, login_management, get_login_url):
    """Test that you can successfully log in as an administrator user"""
    response = client.post(get_login_url, login_management, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"role": "MANAGEMENT"}


@pytest.mark.django_db
def test_general_user_can_login(client, login_general, get_login_url):
    """Test that you can successfully log in as a general user"""
    response = client.post(get_login_url, login_general, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"role": "GENERAL"}


@pytest.mark.django_db
def test_part_time_user_can_login(client, login_part_time, get_login_url):
    """Test that you can successfully log in as a part-time user"""
    response = client.post(get_login_url, login_part_time, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"role": "PART_TIME"}


@pytest.mark.django_db
def test_user_cannot_login_with_incorrect_password(
    client, login_management, get_login_url
):
    """Test that you cannot log in with the wrong password"""
    login_management["password"] = "test6789"
    response = client.post(get_login_url, login_management, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {
        "msg": "Employee number or password is incorrect"
    }


@pytest.mark.django_db
def test_user__cannot_login_with_incorrect_password(
    client, login_management, get_login_url
):
    """Test that you cannot log in with the wrong password"""
    login_management["password"] = "test6789"
    response = client.post(get_login_url, login_management, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {
        "msg": "Employee number or password is incorrect"
    }


@pytest.mark.django_db
def test_user_cannot_login_without_password(
    client, login_management, get_login_url
):
    """Test that you cannot log in without a password"""
    login_management["password"] = None
    response = client.post(get_login_url, login_management, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_user_cannot_login_without_employee_number(
    client, login_management, get_login_url
):
    """Test that you cannot log in without an employee number"""
    login_management["employee_number"] = None
    response = client.post(get_login_url, login_management, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_user_cannot_login_with_employee_number_that_does_not_exist(
    client, login_management, get_login_url
):
    """Test that you cannot log in with a non-existing employee number"""
    login_management["employee_number"] = "12345678"
    response = client.post(get_login_url, login_management, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_user_can_logout(client, login_management, get_login_url):
    """Test that you can log out successfully"""
    login(client, login_management)
    response = client.post(get_login_url, login_management, format="json")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_user_cannot_logout_without_login(
    client, login_management, get_login_url
):
    """Tested to return 200 even if not logged in"""
    response = client.post(get_login_url, login_management, format="json")
    assert response.status_code == status.HTTP_200_OK
