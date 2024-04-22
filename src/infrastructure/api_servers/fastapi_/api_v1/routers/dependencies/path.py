import typing as t

from fastapi import Depends, Path

from .. import schemas


def __get_user_id_from_path(id_: t.Annotated[int, Path(alias="id", gt=0)]) -> schemas.users.UserIdSchema:
    return schemas.users.UserIdSchema(id=id_)


UserIdFromPathDependency = t.Annotated[schemas.users.UserIdSchema, Depends(__get_user_id_from_path)]
