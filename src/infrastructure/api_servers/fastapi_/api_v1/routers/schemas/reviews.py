from pydantic import Field

from common import StrictBaseModel, stars
from domain import entities


class ReviewIdSchema(StrictBaseModel):
    id: int = Field(gt=0, examples=[871])

    def to_entity(self) -> entities.review.ReviewId:
        return entities.review.ReviewId(id=self.id)


class CreateReviewSchema(StrictBaseModel):
    stars: float = Field(
        ge=stars.STARS_MIN,
        multiple_of=stars.STAR_STEP,
        le=stars.STARS_MAX,
        examples=["4.5"],
    )
    text: str | None = Field(default=None, examples=["Heartwarming adventure: laughs, tears, pure joy!"])

    def to_review_contents_entity(self) -> entities.review.ReviewContents:
        return entities.review.ReviewContents(stars=self.stars, text=self.text)
