import typing as t

from fastapi import Depends, Path

from .. import schemas


def __get_aliased_id_from_path(alias: str) -> t.Callable[[int], schemas.id_.IdSchema]:
    def __get_id_from_path(id_: t.Annotated[int, Path(alias=alias, gt=0)]) -> schemas.id_.IdSchema:
        return schemas.id_.IdSchema(id=id_)

    return __get_id_from_path


UserIdFromPathDependency = t.Annotated[schemas.users.UserIdSchema, Depends(__get_aliased_id_from_path("user_id"))]
MovieIdFromPathDependency = t.Annotated[schemas.movies.MovieIdSchema, Depends(__get_aliased_id_from_path("movie_id"))]
ReviewIdFromPathDependency = t.Annotated[
    schemas.reviews.ReviewIdSchema, Depends(__get_aliased_id_from_path("review_id"))
]
