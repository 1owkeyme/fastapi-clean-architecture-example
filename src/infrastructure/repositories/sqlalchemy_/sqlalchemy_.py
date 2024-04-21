import typing as t
from asyncio import current_task
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)

from domain import entities, usecases
from domain.entities.movie import MovieId, MovieInfo
from domain.entities.review import ReviewId, ReviewInfo

from . import models


class SQLAlchemy(
    usecases.user.interfaces.UserRepository,
    usecases.movie.interfaces.MovieRepository,
    usecases.review.interfaces.ReviewRepository,
):
    def __init__(self, url: str, echo: bool = False) -> None:
        engine = create_async_engine(url=url, echo=echo)
        self._session_factory = async_sessionmaker(
            bind=engine,
            autoflush=False,
            expire_on_commit=False,
        )

    @asynccontextmanager
    async def _get_scoped_session(
        self,
    ) -> t.AsyncIterator[async_scoped_session[AsyncSession]]:
        scoped_session = async_scoped_session(
            self._session_factory, scopefunc=current_task
        )
        yield scoped_session
        await scoped_session.close()

    async def create_user(
        self,
        safe_credentials: entities.user.SafeCredentials,
    ) -> None:
        user = models.User(
            username=safe_credentials.username,
            hashed_password_hex=safe_credentials.hashed_password_hex,
        )
        async with self._get_scoped_session() as session:
            session.add(user)
            await session.commit()

    async def create_movie(self, info: MovieInfo) -> None:
        print(f"Created new movie: {info}")

    async def create_review(self, info: ReviewInfo) -> None:
        print(f"Created new review: {info}")

    async def delete_review(self, id_: ReviewId) -> None:
        print(f"Deleted review: {id_}")

    async def delete_movie(self, id_: MovieId) -> None:
        print(f"Deleted movie: {id_}")
