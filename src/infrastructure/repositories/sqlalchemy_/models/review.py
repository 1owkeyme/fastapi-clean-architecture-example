import typing as t

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Integer, Text

from common import StrictBaseModel
from domain import entities

from .base import Base
from .constants import TableName
from .movie import MovieRelationMixin
from .user import UserRelationMixin


class Review(Base, UserRelationMixin, MovieRelationMixin):
    __tablename__ = TableName.REVIEWS

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "movie_id",
            name="idx_unique_user_movie",
        ),
    )

    _user_id_unique = False  # separate compound unique index created
    _user_back_populates = TableName.REVIEWS

    _movie_id_unique = False  # separate compound unique index created
    _movie_back_populates = TableName.REVIEWS

    stars_10x: Mapped[int] = mapped_column(Integer())
    text: Mapped[str | None] = mapped_column(Text())

    def to_review_id_entity(self) -> entities.review.ReviewId:
        return entities.review.ReviewId(id=self.id)

    def to_review_for_user_entity(self) -> entities.review.ReviewForUser:
        return entities.review.ReviewForUser(
            id=self.id,
            stars=self.stars_10x / 10,
            text=self.text,
            movie=self.movie.to_movie_entity(),
        )


class ReviewContents(StrictBaseModel):
    stars_10x: int
    text: str | None = None

    @classmethod
    def from_review_contents_entity(cls, review_contents_entity: entities.review.ReviewContents) -> t.Self:
        return cls(
            stars_10x=int(review_contents_entity.stars * 10),
            text=review_contents_entity.text,
        )
