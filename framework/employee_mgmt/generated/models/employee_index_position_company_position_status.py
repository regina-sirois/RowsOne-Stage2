from enum import StrEnum


class EmployeeIndexPositionCompanyPositionStatus(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)
