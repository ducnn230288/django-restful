from rest_framework import serializers

from application.models import User


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""

    class Meta:
        model = User
        fields = ["id", "employee_number", "username", "email", "role"]
        read_only_fields = ["id", "created_at", "updated_at"]


class LoginSerializer(serializers.ModelSerializer):
    """Login serializer"""

    employee_number = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ["employee_number", "password"]


class EmailSerializer(serializers.Serializer):
    """Email serializer"""

    email = serializers.EmailField(max_length=255)
