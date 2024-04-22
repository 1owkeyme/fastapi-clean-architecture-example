from pydantic import Field

from common import StrictBaseModel, stars

from .movie import Movie
from .user import UserPublic


class ReviewId(StrictBaseModel):
    id: int


class ReviewContents(StrictBaseModel):
    stars: float = Field(
        ge=stars.STARS_MIN,
        multiple_of=stars.STAR_STEP,
        le=stars.STARS_MAX,
    )
    text: str | None = None


class ReviewForUser(ReviewId, ReviewContents):
    movie: Movie


class ReviewForMovie(ReviewId, ReviewContents):
    user: UserPublic
