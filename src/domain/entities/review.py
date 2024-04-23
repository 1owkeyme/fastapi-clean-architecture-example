from pydantic import Field

from common import StrictBaseModel, stars

from .id_ import Id
from .movie import Movie
from .user import UserPublic


class ReviewInfo(StrictBaseModel):
    stars: float = Field(
        ge=stars.STARS_MIN,
        multiple_of=stars.STAR_STEP,
        le=stars.STARS_MAX,
    )
    text: str | None = None


class ReviewMovieInfo(StrictBaseModel):
    movie: Movie


class ReviewUserInfo(StrictBaseModel):
    user: UserPublic


class ReviewForUser(Id, ReviewInfo, ReviewMovieInfo):
    movie: Movie


class ReviewForMovie(Id, ReviewInfo, ReviewUserInfo):
    user: UserPublic


class Review(Id, ReviewInfo, ReviewUserInfo, ReviewMovieInfo):
    pass
