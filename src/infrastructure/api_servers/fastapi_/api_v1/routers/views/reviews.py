import typing as t

from pydantic import Field

from common import StrictBaseModel, stars
from domain import entities

from .id_ import Id
from .movie import Movie
from .users import UserPublic


class ReviewId(Id):
    @classmethod
    def from_review_id_entity(cls, review_id_entity: entities.review.ReviewId) -> t.Self:
        return cls(id=review_id_entity.id)


class ReviewContents(StrictBaseModel):
    stars: float = Field(
        ge=stars.STARS_MIN,
        multiple_of=stars.STAR_STEP,
        le=stars.STARS_MAX,
        examples=["4.5"],
    )
    text: str | None = Field(default=None, examples=["Heartwarming adventure: laughs, tears, pure joy!"])


class ReviewMovieContents(StrictBaseModel):
    movie: Movie


class ReviewUserContents(StrictBaseModel):
    user: UserPublic


class ReviewForUser(ReviewId, ReviewContents, ReviewMovieContents):
    @classmethod
    def from_entity(cls, entity: entities.review.ReviewForUser) -> t.Self:
        return cls(
            id=entity.id,
            stars=entity.stars,
            text=entity.text,
            movie=Movie.from_movie_entity(movie=entity.movie),
        )


class ReviewForMovie(ReviewId, ReviewContents, ReviewUserContents):
    @classmethod
    def from_entity(cls, entity: entities.review.ReviewForMovie) -> t.Self:
        return cls(
            id=entity.id,
            stars=entity.stars,
            text=entity.text,
            user=UserPublic.from_entity(entity=entity.user),
        )


class Review(ReviewId, ReviewContents, ReviewUserContents, ReviewMovieContents):
    @classmethod
    def from_entity(cls, entity: entities.review.Review) -> t.Self:
        return cls(
            id=entity.id,
            stars=entity.stars,
            text=entity.text,
            user=UserPublic.from_entity(entity.user),
            movie=Movie.from_entity(entity.movie),
        )
