from dataclasses import dataclass
from uuid import UUID


@dataclass
class Company:
    id: UUID
    name: str
    department_ids: list[int]
    position_ids: list[int]
    site_ids: list[int]
