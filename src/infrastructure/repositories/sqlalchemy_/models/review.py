import typing as t

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Integer, Text

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

    @classmethod
    def from_review_info_enitity(cls, review_entity: entities.review.ReviewInfo) -> t.Self:
        return cls(
            stars_x10=int(review_entity.stars * 10),
            text=review_entity.text,
            user_id=review_entity.user_id,
            movie_id=review_entity.movie_id,
        )

    def to_review_entity(self) -> entities.review.Review:
        return entities.review.Review(
            id=self.id,
            user_id=self.user_id,
            movie_id=self.movie_id,
            stars=self.stars_10x / 10,
            text=self.text,
        )
