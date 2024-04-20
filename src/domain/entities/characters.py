from common import StrictBaseModel

from .items import Item


class Character(StrictBaseModel):
    name: str
    inventory: list[Item]
