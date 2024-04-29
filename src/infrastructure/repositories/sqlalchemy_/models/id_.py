import typing as t

from sqlalchemy.orm import Mapped, mapped_column

from domain import entities

from .base import Base


class Id(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)

    def to_id_entity(self) -> entities.Id:
        return entities.Id(id=self.id)

    @classmethod
    def id_from_entity(cls, entity: entities.Id) -> t.Self:
        return cls(id=entity.id)
