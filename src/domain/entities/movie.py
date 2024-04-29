from datetime import timedelta

from common import StrictBaseModel

from .id_ import Id


class MovieInfo(StrictBaseModel):
    title: str
    duration: timedelta


class Movie(Id, MovieInfo):
    pass
