import pytest
from rest_framework import status

from application.tests.common_method import login


@pytest.fixture
def get_user_url():
    return "/api/users"


@pytest.fixture
def get_user_details_url(id):
    return f"/api/users/{id}"


@pytest.mark.django_db
def test_management_user_can_list_users(
    client, login_management, get_user_url
):
    """Test that allows an administrator user to display a list of users"""
    login(client, login_management)
    response = client.get(get_user_url, format="json")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_general_user_can_list_users(client, login_management, get_user_url):
    """Test that allows a general user to display a list of users"""
    login(client, login_management)
    response = client.get(get_user_url, format="json")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_sales_user_can_list_users(client, login_part_time, get_user_url):
    """Test that allows part-time users to display a list of users"""
    login(client, login_part_time)
    response = client.get(get_user_url, format="json")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_user_cannot_list_users_without_login(client, get_user_url):
    """Test of not being able to display list of users without login"""
    response = client.get(get_user_url, format="json")
    assert response.status_code == status.HTTP_403_FORBIDDEN
