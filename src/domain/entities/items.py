from common import StrictBaseModel


class Item(StrictBaseModel):
    name: str
    description: str
    price: int
