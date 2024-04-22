from datetime import timedelta

from pydantic import ConfigDict, Field

from common import StrictBaseModel
from domain import entities

from .id_ import IdSchema


class CreateMovieSchema(StrictBaseModel):
    model_config = ConfigDict(ser_json_timedelta="float")

    title: str = Field(examples=["The Great Gatsby"])
    duration: timedelta = Field(strict=False, examples=["P0DT2H33M0S"])

    def to_movie_info_entity(self) -> entities.movie.MovieInfo:
        return entities.movie.MovieInfo(
            title=self.title,
            duration=self.duration,
        )


class MovieIdSchema(IdSchema):
    def to_entity(self) -> entities.movie.MovieId:
        return entities.movie.MovieId(id=self.id)
