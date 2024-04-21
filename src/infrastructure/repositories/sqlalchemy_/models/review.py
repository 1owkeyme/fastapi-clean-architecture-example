from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Integer, Text

from .base import Base
from .constants import TableName
from .movie import MovieRelationMixin
from .user import UserRelationMixin


class Review(Base, UserRelationMixin, MovieRelationMixin):
    __tablename__ = TableName.REVIEWS

    __table_args__ = (
        UniqueConstraint(
            UserRelationMixin.user_id,
            MovieRelationMixin.movie_id,
            name="idx_unique_user_movie",
        ),
    )
    _user_id_unique = False  # separate compound unique index created
    _user_back_populates = TableName.REVIEWS

    _movie_id_unique = False  # separate compound unique index created
    _movie_back_populates = TableName.REVIEWS

    stars_10x: Mapped[int] = mapped_column(Integer())
    text: Mapped[str | None] = mapped_column(Text())
