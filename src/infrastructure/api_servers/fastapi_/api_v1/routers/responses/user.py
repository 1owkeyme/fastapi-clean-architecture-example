import typing as t

from common import StrictBaseModel

from .. import schemas
from . import base


class GetAllUsersResult(StrictBaseModel):
    users: list[schemas.user.UserPublic]


class GetAllUsersResponse(base.SuccessResponse):
    result: GetAllUsersResult

    @classmethod
    def new(cls, users: list[schemas.user.UserPublic]) -> t.Self:
        return cls(result=GetAllUsersResult(users=users))


class GetUserByIdResult(StrictBaseModel):
    user: schemas.user.UserPublic


class GetUserByIdResponse(base.SuccessResponse):
    result: GetUserByIdResult

    @classmethod
    def new(cls, user: schemas.user.UserPublic) -> t.Self:
        return cls(result=GetUserByIdResult(user=user))


class CreateUserResult(schemas.user.UserId):
    pass


class CreateUserResponse(base.SuccessResponse):
    result: CreateUserResult

    @classmethod
    def new(cls, id_: int) -> t.Self:
        return cls(result=CreateUserResult(user_id=id_))


class DeleteUserByIdResult(schemas.user.UserId):
    pass


class DeleteUserByIdResponse(base.SuccessResponse):
    result: DeleteUserByIdResult

    @classmethod
    def new(cls, id_: int) -> t.Self:
        return cls(result=DeleteUserByIdResult(user_id=id_))


class GetAllUserReviewsByIdResult(StrictBaseModel):
    reviews: list[schemas.review.ReviewForUser]


class GetAllUserReviewsByIdResponse(base.SuccessResponse):
    result: GetAllUserReviewsByIdResult

    @classmethod
    def new(cls, reviews_for_user: list[schemas.review.ReviewForUser]) -> t.Self:
        return cls(result=GetAllUserReviewsByIdResult(reviews=reviews_for_user))


class NoUserFoundErrorResult(base.ErrorResult):
    code: base.ErrorCode = base.ErrorCode.USER_NOT_FOUND
    message: str = "User not found"


class UserNotFoundErrorResponse(base.error.ErrorResponse):
    error: NoUserFoundErrorResult

    @classmethod
    def new(cls) -> t.Self:
        return cls(error=NoUserFoundErrorResult())


class UserAlreadyExistsErrorResult(base.ErrorResult):
    code: base.ErrorCode = base.ErrorCode.MOVIE_NOT_FOUND
    message: str = "Movie already exists"


class UserAlreadyExistsErrorResponse(base.error.ErrorResponse):
    error: UserAlreadyExistsErrorResult

    @classmethod
    def new(cls) -> t.Self:
        return cls(error=UserAlreadyExistsErrorResult())


class FirstSuperUserDeleteForbiddenErrorResult(base.ErrorResult):
    code: base.ErrorCode = base.ErrorCode.FIRST_SUPER_USER_DELETE_FORBIDDEN
    message: str = "Can't delete first super user"


class FirstSuperUserDeleteForbiddenErrorResponse(base.error.ErrorResponse):
    error: FirstSuperUserDeleteForbiddenErrorResult

    @classmethod
    def new(cls) -> t.Self:
        return cls(error=FirstSuperUserDeleteForbiddenErrorResult())
