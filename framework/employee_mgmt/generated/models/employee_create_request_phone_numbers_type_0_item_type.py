from enum import StrEnum


class EmployeeCreateRequestPhoneNumbersType0ItemType(StrEnum):
    EMERGENCY = "emergency"
    HOME = "home"
    MOBILE = "mobile"
    OTHER = "other"
    WORK = "work"

    def __str__(self) -> str:
        return str(self.value)
