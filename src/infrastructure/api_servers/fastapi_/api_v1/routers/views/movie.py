import typing as t
from datetime import timedelta

from common import StrictBaseModel
from domain import entities


class MovieId(StrictBaseModel):
    id: int

    @classmethod
    def from_entity(cls, id_: entities.movie.MovieId) -> t.Self:
        return cls(id=id_.id)


class MovieInfo(StrictBaseModel):
    title: str
    duration: timedelta


class Movie(MovieId, MovieInfo):
    @classmethod
    def from_movie_entity(cls, movie: entities.movie.Movie) -> t.Self:
        return cls(
            id=movie.id,
            title=movie.title,
            duration=movie.duration,
        )
