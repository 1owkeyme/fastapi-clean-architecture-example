from pydantic import Field

from common import StrictBaseModel, stars


class ReviewId(StrictBaseModel):
    id: int


class ReviewInfo(StrictBaseModel):
    user_id: int
    movie_id: int
    stars: float = Field(
        ge=stars.STARS_MIN,
        multiple_of=stars.STAR_STEP,
        le=stars.STARS_MAX,
    )
    text: str | None = None


class ReviewFor(ReviewId, ReviewInfo):
    pass
