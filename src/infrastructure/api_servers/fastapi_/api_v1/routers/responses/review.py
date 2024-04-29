import typing as t

from common import StrictBaseModel

from .. import schemas
from . import base


class GetReviewByIdResult(StrictBaseModel):
    review: schemas.review.Review


class GetReviewByIdResponse(base.SuccessResponse):
    result: GetReviewByIdResult

    @classmethod
    def new(cls, review: schemas.review.Review) -> t.Self:
        return cls(result=GetReviewByIdResult(review=review))


class CreateReviewResult(schemas.review.ReviewId):
    pass


class CreateReviewResponse(base.SuccessResponse):
    result: CreateReviewResult

    @classmethod
    def new(cls, id_: int) -> t.Self:
        return cls(result=CreateReviewResult(review_id=id_))


class DeleteReviewByIdResult(schemas.review.ReviewId):
    pass


class DeleteReviewByIdResponse(base.SuccessResponse):
    result: DeleteReviewByIdResult

    @classmethod
    def new(cls, id_: int) -> t.Self:
        return cls(result=DeleteReviewByIdResult(review_id=id_))


class ReviewNotFoundErrorResult(base.ErrorResult):
    code: base.ErrorCode = base.ErrorCode.REVIEW_NOT_FOUND
    message: str = "Review not found"


class ReviewNotFoundErrorResponse(base.error.ErrorResponse):
    error: ReviewNotFoundErrorResult

    @classmethod
    def new(cls) -> t.Self:
        return cls(error=ReviewNotFoundErrorResult())


class ReviewAlreadyExistsErrorResult(base.ErrorResult):
    code: base.ErrorCode = base.ErrorCode.REVIEW_ALREADY_EXISTS
    message: str = "Review already exists"


class ReviewAlreadyExistsErrorResponse(base.error.ErrorResponse):
    error: ReviewAlreadyExistsErrorResult

    @classmethod
    def new(cls) -> t.Self:
        return cls(error=ReviewAlreadyExistsErrorResult())
