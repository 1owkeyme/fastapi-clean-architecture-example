from pydantic import Field

from common import StrictBaseModel, stars
from domain import entities

from .id_ import IdSchema


class ReviewIdSchema(IdSchema):
    def to_entity(self) -> entities.review.ReviewId:
        return entities.review.ReviewId(id=self.id)


class CreateReviewSchema(StrictBaseModel):
    stars: float = Field(
        ge=stars.STARS_MIN,
        multiple_of=stars.STAR_STEP,
        le=stars.STARS_MAX,
    )
    text: str | None = None

    def to_review_contents_entity(self) -> entities.review.ReviewContents:
        return entities.review.ReviewContents(stars=self.stars, text=self.text)
