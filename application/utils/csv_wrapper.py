"""Module for CSV"""

import csv

from application.models import User
from django.http import HttpResponse


class CSVUserListData:
    """CSV data class for user list"""

    def __init__(self, users: list[User]):
        self.headers = [
            "employee number",
            "name",
            "email address",
            "authority",
        ]
        self.rows = self._create_rows(users)

    @staticmethod
    def _create_rows(users: list[User]):
        """generate columns"""
        rows = []
        for user in users:
            rows.append(
                [
                    user.employee_number,
                    user.username,
                    user.employee_number,
                    user.role,
                ]
            )
        return rows


class CSVResponseWrapper:
    """csv wrapper class"""

    def __init__(self, filename: str):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = f'attachment; filename="{filename}"'
        self.response = response

    def write_response(self, csv_data: CSVUserListData):
        """Write csv to response"""
        writer = csv.writer(self.response)
        writer.writerow(csv_data.headers)
        for row in csv_data.rows:
            writer.writerow(row)
