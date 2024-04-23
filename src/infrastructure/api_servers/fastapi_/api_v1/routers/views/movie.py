import typing as t
from datetime import timedelta

from pydantic import Field

from common import StrictBaseModel
from domain import entities


class MovieId(StrictBaseModel):
    id: int = Field(gt=0, examples=[502])

    @classmethod
    def from_entity(cls, id_: entities.movie.MovieId) -> t.Self:
        return cls(id=id_.id)


class MovieInfo(StrictBaseModel):
    title: str = Field(examples=["The Great Gatsby"])
    duration: timedelta = Field(strict=False, examples=["P0DT2H33M0S"])


class Movie(MovieId, MovieInfo):
    @classmethod
    def from_movie_entity(cls, movie: entities.movie.Movie) -> t.Self:
        return cls(
            id=movie.id,
            title=movie.title,
            duration=movie.duration,
        )
