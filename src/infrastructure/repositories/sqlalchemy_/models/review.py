import typing as t

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Integer, Text

from domain import entities

from .base import Base
from .constants import TableName
from .id_ import Id
from .movie import MovieRelationMixin
from .user import UserRelationMixin


class ReviewInfo(Base):
    __abstract__ = True

    stars_10x: Mapped[int] = mapped_column(Integer())
    text: Mapped[str | None] = mapped_column(Text())

    @classmethod
    def review_info_from_entity(cls, entity: entities.review.ReviewInfo) -> t.Self:
        return cls(stars_10x=int(entity.stars * 10), text=entity.text)


class Review(Id, ReviewInfo, UserRelationMixin, MovieRelationMixin):
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

    def to_entity(self) -> entities.review.Review:
        return entities.review.Review(
            id=self.id,
            movie=self.movie.to_movie_entity(),
            user=self.user.to_user_public_entity(),
            stars=self.stars_10x / 10,
            text=self.text,
        )

    def to_review_for_user_entity(self) -> entities.review.ReviewForUser:
        return entities.review.ReviewForUser(
            id=self.id,
            stars=self.stars_10x / 10,
            text=self.text,
            movie=self.movie.to_movie_entity(),
        )

    def to_review_for_movie_entity(self) -> entities.review.ReviewForMovie:
        return entities.review.ReviewForMovie(
            id=self.id,
            stars=self.stars_10x / 10,
            text=self.text,
            user=self.user.to_user_public_entity(),
        )
