import pytest
from collections.abc import Generator
from typing import Any
from dotenv import load_dotenv
from framework import Environment, get_environment

load_dotenv()


@pytest.fixture(scope="session")
def environment() -> Generator[Environment, Any, None]:
    try:
        yield get_environment()
    except ValueError as exc:
        raise ValueError("Environment name is not valid or not set") from exc
    except Exception as exc:
        raise ValueError("Failed to get environment") from exc

