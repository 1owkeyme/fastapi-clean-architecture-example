import typing as t

from pydantic import Field

from common import StrictBaseModel, stars
from domain import entities


class ReviewId(StrictBaseModel):
    id: int

    @classmethod
    def from_review_id_entity(cls, review_id_entity: entities.review.ReviewId) -> t.Self:
        return cls(id=review_id_entity.id)

    def to_review_id_entity(self) -> entities.review.ReviewId:
        return entities.review.ReviewId(id=self.id)


class ReviewForUser(ReviewId):
    stars: float = Field(
        ge=stars.STARS_MIN,
        multiple_of=stars.STAR_STEP,
        le=stars.STARS_MAX,
    )
    text: str | None = None
