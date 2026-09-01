from enum import StrEnum


class EmployeeUpdateRequestPreferredLanguage(StrEnum):
    AR = "ar"
    EN = "en"
    ES = "es"
    FR = "fr"
    KO = "ko"
    OTHER = "other"
    PT = "pt"
    RU = "ru"
    TL = "tl"
    VI = "vi"
    ZH = "zh"

    def __str__(self) -> str:
        return str(self.value)
