import typing as t

from common import StrictBaseModel

from ..movie import Movie, MovieId
from ..reviews import ReviewForMovie
from . import base


class GetMovieByIdResult(StrictBaseModel):
    movie: Movie


class GetMovieByIdResponse(base.SuccessResponse):
    result: GetMovieByIdResult

    @classmethod
    def new(cls, movie: Movie) -> t.Self:
        return cls(result=GetMovieByIdResult(movie=movie))


class GetAllMoviesResult(StrictBaseModel):
    movies: list[Movie]


class GetAllMoviesResponse(StrictBaseModel):
    result: GetAllMoviesResult

    @classmethod
    def new(cls, movies: list[Movie]) -> t.Self:
        return cls(result=GetAllMoviesResult(movies=movies))


class CreateMovieResult(MovieId):
    pass


class CreateMovieResponse(base.SuccessResponse):
    result: CreateMovieResult

    @classmethod
    def new(cls, id_: MovieId) -> t.Self:
        return cls(result=CreateMovieResult(id=id_.id))


class DeleteMovieResult(MovieId):
    pass


class DeleteMovieResponse(base.SuccessResponse):
    result: DeleteMovieResult

    @classmethod
    def new(cls, id_: MovieId) -> t.Self:
        return cls(result=DeleteMovieResult(id=id_.id))


class GetAllMovieReviewsResult(StrictBaseModel):
    reviews: list[ReviewForMovie]


class GetAllMovieReviewsResponse(base.SuccessResponse):
    result: GetAllMovieReviewsResult

    @classmethod
    def new(cls, reviews_for_movie: list[ReviewForMovie]) -> t.Self:
        return cls(result=GetAllMovieReviewsResult(reviews=reviews_for_movie))
