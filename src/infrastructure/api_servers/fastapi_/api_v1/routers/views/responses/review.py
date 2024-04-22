import typing as t

from common import StrictBaseModel

from ..reviews import Review, ReviewId
from . import base


class GetReviewByIdResult(StrictBaseModel):
    review: Review


class GetReviewByIdResponse(base.SuccessResponse):
    result: GetReviewByIdResult

    @classmethod
    def new(cls, review: Review) -> t.Self:
        return cls(result=GetReviewByIdResult(review=review))


class CreateReviewResult(ReviewId):
    pass


class CreateReviewResponse(base.SuccessResponse):
    result: CreateReviewResult

    @classmethod
    def new(cls, review_id: ReviewId) -> t.Self:
        return cls(result=CreateReviewResult(id=review_id.id))


class DeleteReviewResult(ReviewId):
    pass


class DeleteReviewResponse(base.SuccessResponse):
    result: DeleteReviewResult

    @classmethod
    def new(cls, id_: ReviewId) -> t.Self:
        return cls(result=DeleteReviewResult(id=id_.id))
