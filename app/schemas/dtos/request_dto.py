from dataclasses import dataclass

from app.schemas.dtos.base_dto import BaseDTO


@dataclass(repr=True)
class RequestDTO(BaseDTO):
    name: str
    email: str
