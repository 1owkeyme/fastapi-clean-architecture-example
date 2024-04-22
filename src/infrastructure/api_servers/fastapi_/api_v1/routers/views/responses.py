import typing as t

from common import StrictBaseModel
from infrastructure.api_servers import responses

from .reviews import ReviewForUser
from .users import UserId, UserPublic


class GetAllUsersResult(StrictBaseModel):
    users: list[UserPublic]


class CreateUserResult(UserId):
    pass


class GetAllUsersResponse(responses.base.SuccessResponse):
    result: GetAllUsersResult

    @classmethod
    def new(cls, users: list[UserPublic]) -> t.Self:
        return cls(result=GetAllUsersResult(users=users))


class CreateUserResponse(responses.base.SuccessResponse):
    result: CreateUserResult

    @classmethod
    def new(cls, user_id: UserId) -> t.Self:
        return cls(result=CreateUserResult(id=user_id.id))


class GetAllUserReviewsResult(StrictBaseModel):
    reviews: list[ReviewForUser]


class GetAllUserReviewsResponse(responses.base.SuccessResponse):
    result: GetAllUserReviewsResult

    @classmethod
    def new(cls, reviews_for_user: list[ReviewForUser]) -> t.Self:
        return cls(result=GetAllUserReviewsResult(reviews=reviews_for_user))
