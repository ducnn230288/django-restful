from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from application.emails import send_welcome_email
from application.models.user import User
from application.permissions import (
    IsGeneralUser,
    IsManagementUser,
    IsPartTimeUser,
    IsSuperUser,
)
from application.serializers.user import EmailSerializer, UserSerializer
from application.utils.csv_wrapper import CSVResponseWrapper, CSVUserListData


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "send_invite_user_mail":
            return EmailSerializer
        else:
            return UserSerializer

    @action(detail=False, methods=["POST"])
    def send_invite_user_mail(self, request):
        """Send an invitation email to the specified email address

        Args:
            request: request

        Returns:
            HttpResponse
        """
        serializer = self.get_serializer(data=request.data)
        # Returns 400 if validation fails
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        # Method for sending email
        send_welcome_email(email=email)
        return HttpResponse()

    # You can grant permissions according to the table above using the get_permissions method.
    def get_permissions(self):
        if self.action in {
            "update",
            "partial_update",
            "send_invite_user_mail",
        }:
            permission_classes = [IsManagementUser]
        elif self.action == "create":
            permission_classes = [IsGeneralUser]
        elif self.action == "destroy":
            permission_classes = [IsSuperUser]
        elif self.action in ["list", "retrieve"]:
            permission_classes = [IsPartTimeUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(methods=["post"], detail=False)
    def export(self, request):
        """
        API to export user list in CSV format
        Returns:
            CSV file
        """
        csvWrapper = CSVResponseWrapper("user_data.csv")
        csv_data = CSVUserListData(self.queryset)
        csvWrapper.write_response(csv_data)

        return csvWrapper.response
