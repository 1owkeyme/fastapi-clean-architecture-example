import typing as t

from common import StrictBaseModel

from ..reviews import ReviewForUser
from ..users import UserId, UserPublic
from . import base


class GetAllUsersResult(StrictBaseModel):
    users: list[UserPublic]


class GetAllUsersResponse(base.SuccessResponse):
    result: GetAllUsersResult

    @classmethod
    def new(cls, users: list[UserPublic]) -> t.Self:
        return cls(result=GetAllUsersResult(users=users))


class GetUserByIdResult(StrictBaseModel):
    user: UserPublic


class GetUserByIdResponse(base.SuccessResponse):
    result: GetUserByIdResult

    @classmethod
    def new(cls, user: UserPublic) -> t.Self:
        return cls(result=GetUserByIdResult(user=user))


class CreateUserResult(UserId):
    pass


class CreateUserResponse(base.SuccessResponse):
    result: CreateUserResult

    @classmethod
    def new(cls, user_id: UserId) -> t.Self:
        return cls(result=CreateUserResult(id=user_id.id))


class GetAllUserReviewsResult(StrictBaseModel):
    reviews: list[ReviewForUser]


class GetAllUserReviewsResponse(base.SuccessResponse):
    result: GetAllUserReviewsResult

    @classmethod
    def new(cls, reviews_for_user: list[ReviewForUser]) -> t.Self:
        return cls(result=GetAllUserReviewsResult(reviews=reviews_for_user))
