from datetime import timedelta

from common import StrictBaseModel


class Movie(StrictBaseModel):
    title: str
    duration: timedelta
