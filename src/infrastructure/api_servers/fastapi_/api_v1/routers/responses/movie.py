import typing as t

from common import StrictBaseModel

from .. import schemas
from . import base


class GetMovieByIdResult(StrictBaseModel):
    movie: schemas.movie.Movie


class GetMovieByIdResponse(base.SuccessResponse):
    result: GetMovieByIdResult

    @classmethod
    def new(cls, movie: schemas.movie.Movie) -> t.Self:
        return cls(result=GetMovieByIdResult(movie=movie))


class GetAllMoviesResult(StrictBaseModel):
    movies: list[schemas.movie.Movie]


class GetAllMoviesResponse(StrictBaseModel):
    result: GetAllMoviesResult

    @classmethod
    def new(cls, movies: list[schemas.movie.Movie]) -> t.Self:
        return cls(result=GetAllMoviesResult(movies=movies))


class CreateMovieResult(schemas.movie.MovieId):
    pass


class CreateMovieResponse(base.SuccessResponse):
    result: CreateMovieResult

    @classmethod
    def new(cls, id_: int) -> t.Self:
        return cls(result=CreateMovieResult(movie_id=id_))


class DeleteMovieResult(schemas.movie.MovieId):
    pass


class DeleteMovieByIdResponse(base.SuccessResponse):
    result: DeleteMovieResult

    @classmethod
    def new(cls, id_: int) -> t.Self:
        return cls(result=DeleteMovieResult(movie_id=id_))


class GetAllMovieReviewsByIdResult(StrictBaseModel):
    reviews: list[schemas.review.ReviewForMovie]


class GetAllMovieReviewsByIdResponse(base.SuccessResponse):
    result: GetAllMovieReviewsByIdResult

    @classmethod
    def new(cls, reviews_for_movie: list[schemas.review.ReviewForMovie]) -> t.Self:
        return cls(result=GetAllMovieReviewsByIdResult(reviews=reviews_for_movie))
