# Environment management for test framework, uses environment variables to set the environment name,
# and loads the urls and users appropriate to the environment.
import os
from dataclasses import dataclass
from functools import lru_cache

from framework.common.env.urls import Urls
from framework.common.env.users import Users

VALID_ENVS = {"dev", "staging", "prod"}

@dataclass(frozen=True)
class Environment:
    name: str
    urls: Urls
    users: Users

    def __post_init__(self):
        if self.name not in VALID_ENVS:
            raise ValueError(
                f"Invalid environment {self.name!r}. Must be one of {sorted(VALID_ENVS)}"
            )

@lru_cache(maxsize=1)
def get_environment() -> Environment:
    name = os.environ.get("TEST_ENV", "dev").lower()
    return Environment(
        name=name,
        urls=Urls(name),
        users=Users(name),
    )
