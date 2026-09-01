from enum import StrEnum


class EmployeeProfileCompanyStatus(StrEnum):
    ACTIVE = "active"
    CLOSED = "closed"
    PENDING = "pending"
    TERMED = "termed"

    def __str__(self) -> str:
        return str(self.value)
