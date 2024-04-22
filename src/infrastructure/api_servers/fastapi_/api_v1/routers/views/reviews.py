import typing as t

from pydantic import Field

from common import StrictBaseModel, stars
from domain import entities

from .movie import Movie


class ReviewId(StrictBaseModel):
    id: int

    @classmethod
    def from_review_id_entity(cls, review_id_entity: entities.review.ReviewId) -> t.Self:
        return cls(id=review_id_entity.id)

    def to_review_id_entity(self) -> entities.review.ReviewId:
        return entities.review.ReviewId(id=self.id)


class ReviewContents(StrictBaseModel):
    stars: float = Field(
        ge=stars.STARS_MIN,
        multiple_of=stars.STAR_STEP,
        le=stars.STARS_MAX,
    )
    text: str | None = None


class ReviewForUser(ReviewId, ReviewContents):
    movie: Movie

    @classmethod
    def from_entity(cls, entity: entities.review.ReviewForUser) -> t.Self:
        return cls(
            id=entity.id,
            stars=entity.stars,
            text=entity.text,
            movie=Movie.from_entity(movie=entity.movie),
        )
