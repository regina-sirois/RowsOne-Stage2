from enum import StrEnum


class PhoneNumberResourceType(StrEnum):
    EMERGENCY = "emergency"
    HOME = "home"
    MOBILE = "mobile"
    OTHER = "other"
    WORK = "work"

    def __str__(self) -> str:
        return str(self.value)
