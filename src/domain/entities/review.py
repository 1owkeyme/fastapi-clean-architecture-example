from pydantic import Field

from common import StrictBaseModel


_STARS_MIN = 0.0
_STARS_MAX = 5.0
_STAR_STEP = 0.5


class Review(StrictBaseModel):
    movie_id: int
    stars: float = Field(
        ge=_STARS_MIN,
        multiple_of=_STAR_STEP,
        le=_STARS_MAX,
    )
    text: str
