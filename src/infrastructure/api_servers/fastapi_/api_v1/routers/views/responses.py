import typing as t

from common import StrictBaseModel
from infrastructure.api_servers import responses

from .auth import TokenInfo
from .reviews import ReviewForUser
from .users import UserId, UserPublic


class GetAllUsersResult(StrictBaseModel):
    users: list[UserPublic]


class GetAllUsersResponse(responses.base.SuccessResponse):
    result: GetAllUsersResult

    @classmethod
    def new(cls, users: list[UserPublic]) -> t.Self:
        return cls(result=GetAllUsersResult(users=users))


class GetUserByIdResult(StrictBaseModel):
    user: UserPublic


class GetUserByIdResponse(responses.base.SuccessResponse):
    result: GetUserByIdResult

    @classmethod
    def new(cls, user: UserPublic) -> t.Self:
        return cls(result=GetUserByIdResult(user=user))


class CreateUserResult(UserId):
    pass


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


class LoginResult(StrictBaseModel):
    token_info: TokenInfo


class LoginResponse(responses.base.SuccessResponse):
    result: LoginResult

    @classmethod
    def new(cls, token_info: TokenInfo) -> t.Self:
        return cls(result=LoginResult(token_info=token_info))
