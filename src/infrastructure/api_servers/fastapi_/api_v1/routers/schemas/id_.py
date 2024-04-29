import typing as t

from pydantic import Field

from common import StrictBaseModel
from domain import entities


class Id(StrictBaseModel):
    id: int = Field(gt=0, examples=[123])

    def to_id_entity(self) -> entities.Id:
        return entities.Id(id=self.id)

    @classmethod
    def from_id_entity(cls, entity: entities.Id) -> t.Self:
        return cls(id=entity.id)
