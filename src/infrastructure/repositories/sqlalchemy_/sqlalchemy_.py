import typing as t
from asyncio import current_task
from contextlib import asynccontextmanager

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import selectinload

from domain import entities, usecases

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
    async def _get_scoped_session(self) -> t.AsyncIterator[async_scoped_session[AsyncSession]]:
        scoped_session = async_scoped_session(self._session_factory, scopefunc=current_task)
        yield scoped_session
        await scoped_session.close()

    async def get_user_by_id(self, id_entity: entities.user.UserId) -> entities.user.UserPublic:
        async with self._get_scoped_session() as session:
            if (user := await session.get(models.User, id_entity.id)) is not None:
                return user.to_user_public_entity()
            raise usecases.user.interfaces.repository_errors.UserNotFoundError

    async def get_user_private_by_username(self, username_entity: entities.user.Username) -> entities.user.UserPrivate:
        username_model = models.user.Username.from_entity(username_entity)

        stmt = select(models.User).where(models.User.username == username_model.username)
        async with self._get_scoped_session() as session:
            if (user := await session.scalar(stmt)) is not None:
                return user.to_user_private_entity()
            raise usecases.user.interfaces.repository_errors.UserNotFoundError

    async def get_all_users(self) -> list[entities.user.UserPublic]:
        stmt = select(models.User).order_by(models.User.id)
        async with self._get_scoped_session() as session:
            users = (await session.scalars(stmt)).all()

        return [user.to_user_public_entity() for user in users]

    async def create_user(self, safe_credentials_entity: entities.user.SafeCredentials) -> entities.user.UserId:
        user = models.User(
            username=safe_credentials_entity.username,
            hashed_password_hex=safe_credentials_entity.hashed_password_hex,
        )
        async with self._get_scoped_session() as session:
            session.add(user)
            try:
                await session.commit()
            except IntegrityError:
                raise usecases.user.interfaces.repository_errors.UserAlreadyExistsError from None

        return user.to_user_id_entity()

    async def delete_user(self, id_entity: entities.user.UserId) -> None:
        async with self._get_scoped_session() as session:
            if (user := await session.get(models.User, id_entity.id)) is not None:
                await session.delete(user)
            else:
                raise usecases.user.interfaces.repository_errors.UserNotFoundError
            await session.commit()

    async def get_all_user_reviews(self, id_entity: entities.user.UserId) -> list[entities.review.ReviewForUser]:
        stmt = select(models.User).options(selectinload(models.User.reviews)).where(models.User.id == id_entity.id)
        async with self._get_scoped_session() as session:
            if (user := await session.scalar(stmt)) is not None:
                return [review.to_review_for_user_entity() for review in user.reviews]
            raise usecases.user.interfaces.repository_errors.UserNotFoundError

    async def get_movie_by_id(self, id_entity: entities.movie.MovieId) -> entities.movie.Movie:
        async with self._get_scoped_session() as session:
            if (movie := await session.get(models.Movie, id_entity.id)) is not None:
                return movie.to_movie_entity()
            raise usecases.movie.interfaces.repository_errors.MovieNotFoundError

    async def get_all_movies(self) -> list[entities.movie.Movie]:
        stmt = select(models.Movie).order_by(models.Movie.id)
        async with self._get_scoped_session() as session:
            movies = (await session.scalars(stmt)).all()

        return [movie.to_movie_entity() for movie in movies]

    async def create_movie(self, info_entity: entities.movie.MovieInfo) -> None:
        movie = models.Movie.from_movie_info_entity(info_entity)
        async with self._get_scoped_session() as session:
            session.add(movie)
            try:
                await session.commit()
            except IntegrityError:
                raise usecases.movie.interfaces.repository_errors.MovieAlreadyExistsError from None

    async def delete_movie(self, id_entity: entities.movie.MovieId) -> None:
        async with self._get_scoped_session() as session:
            if (movie := await session.get(models.Movie, id_entity.id)) is not None:
                await session.delete(movie)
            else:
                raise usecases.movie.interfaces.repository_errors.MovieNotFoundError
            await session.commit()

    async def get_all_movie_reviews(self, id_entity: entities.movie.MovieId) -> list[entities.review.ReviewForMovie]:
        stmt = select(models.Movie).options(selectinload(models.Movie.reviews)).where(models.Movie.id == id_entity.id)
        async with self._get_scoped_session() as session:
            if (movie := await session.scalar(stmt)) is not None:
                return [review.to_review_entity() for review in movie.reviews]
            raise usecases.movie.interfaces.repository_errors.MovieNotFoundError

    async def get_review_by_id(self, id_entity: entities.review.ReviewId) -> None:
        pass  # TODO:

    async def create_review(
        self,
        user_id_entity: entities.user.UserId,
        movie_id_entity: entities.movie.MovieId,
        contents_entity: entities.review.ReviewContents,
    ) -> entities.review.ReviewId:
        review_contents = models.review.ReviewContents.from_review_contents_entity(
            review_contents_entity=contents_entity
        )
        user_id = models.user.UserId.from_user_id_entity(user_id_entity=user_id_entity)
        movie_id = models.movie.MovieId.from_movie_id_entity(movie_id_entity=movie_id_entity)

        review = models.Review(
            user_id=user_id.id,
            movie_id=movie_id.id,
            stars_10x=review_contents.stars_10x,
            text=review_contents.text,
        )
        async with self._get_scoped_session() as session:
            session.add(review)
            try:
                await session.commit()
            except IntegrityError:
                raise usecases.review.interfaces.repository_errors.ReviewAlreadyExistsError from None

        return review.to_review_id_entity()

    async def delete_review(self, id_entity: entities.review.ReviewId) -> None:
        async with self._get_scoped_session() as session:
            if (review := await session.get(models.Review, id_entity.id)) is not None:
                await session.delete(review)
            else:
                raise usecases.review.interfaces.repository_errors.ReviewNotFoundError
            await session.commit()
