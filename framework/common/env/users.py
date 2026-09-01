# Users management for test framework
# NOTE: 
# - Please keep users in alphabetical order, for ease of maintenance
import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

NOT_FOUND_ERROR = f"Variable not found for environment: {os.getenv("TEST_ENV", None)}"

@dataclass(frozen=True)
class User:
    email: str
    password: str
    client_id: str | None
    client_secret: str | None


class Users:
    environment: str

    def __init__(self, environment: str) -> None:
        self.environment = environment.upper()

    def get_sdet_user(self) -> User:
        email = os.environ.get(f"SDET_EMAIL_{self.environment}")
        password = os.environ.get(f"SDET_PASSWORD_{self.environment}")
        client_id = os.environ.get(f"SDET_CLIENT_ID_{self.environment}", None)
        client_secret = os.environ.get(f"SDET_CLIENT_SECRET_{self.environment}", None)

        if not email or not password:
            raise ValueError(NOT_FOUND_ERROR)

        return User(email=email, password=password, client_id=client_id, client_secret=client_secret)
