from datetime import timedelta

from pydantic import Field

from common import StrictBaseModel
from domain import entities


class CreateMovieSchema(StrictBaseModel):
    title: str = Field(examples=["The Great Gatsby"])
    duration: timedelta

    def to_movie_info_entity(self) -> entities.movie.MovieInfo:
        return entities.movie.MovieInfo(
            title=self.title,
            duration=self.duration,
        )


class DeleteMovieSchema(StrictBaseModel):
    id_: int
    
    
    def to_movie_id_entity(self) -> entities.movie.MovieId:
        return entities.movie.MovieId(
            title=self.title,   
            duration=self.duration,
        )