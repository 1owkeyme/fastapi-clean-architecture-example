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
