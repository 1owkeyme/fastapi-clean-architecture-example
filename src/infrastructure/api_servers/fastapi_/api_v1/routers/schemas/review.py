import typing as t

from pydantic import Field

from common import StrictBaseModel, stars
from domain import entities

from .id_ import Id
from .movie import Movie
from .user import UserPublic


class ReviewInfo(StrictBaseModel):
    stars: float = Field(
        ge=stars.STARS_MIN,
        multiple_of=stars.STAR_STEP,
        le=stars.STARS_MAX,
        examples=["4.5"],
    )
    text: str | None = Field(default=None, examples=["Heartwarming adventure: laughs, tears, pure joy!"])

    def to_entity(self) -> entities.review.ReviewInfo:
        return entities.review.ReviewInfo(stars=self.stars, text=self.text)


class CreateReview(ReviewInfo):
    pass


class ReviewMovieInfo(StrictBaseModel):
    movie: Movie


class ReviewUserInfo(StrictBaseModel):
    user: UserPublic


class ReviewForUser(Id, ReviewInfo, ReviewMovieInfo):
    @classmethod
    def from_entity(cls, entity: entities.review.ReviewForUser) -> t.Self:
        return cls(
            id=entity.id,
            stars=entity.stars,
            text=entity.text,
            movie=Movie.from_movie_entity(movie=entity.movie),
        )


class ReviewForMovie(Id, ReviewInfo, ReviewUserInfo):
    @classmethod
    def from_entity(cls, entity: entities.review.ReviewForMovie) -> t.Self:
        return cls(
            id=entity.id,
            stars=entity.stars,
            text=entity.text,
            user=UserPublic.from_entity(entity=entity.user),
        )


class Review(Id, ReviewInfo, ReviewUserInfo, ReviewMovieInfo):
    @classmethod
    def from_entity(cls, entity: entities.review.Review) -> t.Self:
        return cls(
            id=entity.id,
            stars=entity.stars,
            text=entity.text,
            user=UserPublic.from_entity(entity.user),
            movie=Movie.from_movie_entity(entity.movie),
        )


class ReviewId(StrictBaseModel):
    review_id: int = Field(gt=0, examples=[871])

    @classmethod
    def from_id_entity(cls, entity: entities.Id) -> t.Self:
        return cls(review_id=entity.id)
