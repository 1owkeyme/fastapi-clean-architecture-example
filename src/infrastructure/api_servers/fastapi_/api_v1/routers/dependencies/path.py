import typing as t

from fastapi import Depends, Path

from .. import schemas


def __get_id_from_path(id_: t.Annotated[int, Path(alias="id", gt=0)]) -> schemas.id_.IdSchema:
    return schemas.id_.IdSchema(id=id_)


UserIdFromPathDependency = t.Annotated[schemas.users.UserIdSchema, Depends(__get_id_from_path)]
MovieIdFromPathDependency = t.Annotated[schemas.movies.MovieIdSchema, Depends(__get_id_from_path)]
ReviewIdFromPathDependency = t.Annotated[schemas.reviews.ReviewIdSchema, Depends(__get_id_from_path)]
