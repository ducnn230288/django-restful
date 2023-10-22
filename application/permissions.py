"""
Module for permissions
"""
from rest_framework.permissions import BasePermission

from application.models import User


class IsPartTimeUser(BasePermission):
    def has_permission(self, request, view):
        """Determine whether you are a part-time user

        Args:
            request: request
            view: view

        Returns:
            True if part-time user
            Otherwise False
        """
        if request.user.is_superuser:
            return True

        if request.user.is_authenticated:
            # There is nothing that a part-time user can do that general users and administrative users cannot do,
            # so administrative users are also true.
            if request.user.role in [
                User.Role.PART_TIME,
                User.Role.GENERAL,
                User.Role.MANAGEMENT,
            ]:
                return True
        return False


class IsGeneralUser(BasePermission):
    def has_permission(self, request, view):
        """Determine whether it is a general user

        Args:
            request: request
            view: view
        Returns:
            True for general users
            Otherwise False
        """
        if request.user.is_superuser:
            return True

        if request.user.is_authenticated:
            # Set to True for both general users and administrative users.
            if request.user.role in [
                User.Role.GENERAL,
                User.Role.MANAGEMENT,
            ]:
                return True
        return False


class IsManagementUser(BasePermission):
    def has_permission(self, request, view):
        """Determine whether it is an administrative user

        Args:
            request: request
            view: request

        Returns:
            True if admin user
            Otherwise False
        """
        if request.user.is_superuser:
            return True

        if request.user.is_authenticated:
            if request.user.role == User.Role.MANAGEMENT:
                return True
        return False


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        """Determine whether you are a superuser

        Args:
            request: request
            view: view

        Returns:
            True if superuser
            Otherwise False
        """
        return request.user.is_superuser
