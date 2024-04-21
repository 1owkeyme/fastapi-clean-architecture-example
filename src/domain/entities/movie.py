from datetime import timedelta

from common import StrictBaseModel


class MovieId(StrictBaseModel):
    id: int


class MovieInfo(StrictBaseModel):
    title: str
    duration: timedelta
