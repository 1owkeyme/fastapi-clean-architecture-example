from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload

from domain import entities, usecases

from . import models
from .base import AlchemyBaseRepository


class AlchemyMovieRepository(AlchemyBaseRepository, usecases.interfaces.repositories.MovieRepository):
    def __init__(self, url: str, echo: bool = False) -> None:
        self._scoped_session_factory = self._get_scoped_session_factory(url, echo)

    async def get_movie_by_id(self, id_entity: entities.Id) -> entities.movie.Movie:
        async with self._scoped_session_factory() as session:
            if (movie := await session.get(models.Movie, id_entity.id)) is not None:
                return movie.to_movie_entity()
            raise usecases.interfaces.repositories.movie_errors.MovieNotFoundError

    async def get_all_movies(self) -> list[entities.movie.Movie]:
        stmt = select(models.Movie).order_by(models.Movie.id)
        async with self._scoped_session_factory() as session:
            movies = (await session.scalars(stmt)).all()

        return [movie.to_movie_entity() for movie in movies]

    async def create_movie(self, info_entity: entities.movie.MovieInfo) -> entities.Id:
        movie_info = models.movie.MovieInfo.movie_info_from_entity(info_entity)

        movie = models.Movie(title=movie_info.title, duration=movie_info.duration)

        async with self._scoped_session_factory() as session:
            session.add(movie)
            try:
                await session.commit()
            except IntegrityError:
                raise usecases.interfaces.repositories.movie_errors.MovieAlreadyExistsError from None
        return movie.to_id_entity()

    async def delete_movie_by_id(self, id_entity: entities.Id) -> entities.Id:
        async with self._scoped_session_factory() as session:
            if (movie := await session.get(models.Movie, id_entity.id)) is not None:
                await session.delete(movie)
            else:
                raise usecases.interfaces.repositories.movie_errors.MovieNotFoundError
            await session.commit()
        return id_entity

    async def get_all_movie_reviews_by_id(self, id_entity: entities.Id) -> list[entities.review.ReviewForMovie]:
        stmt = (
            select(models.Movie)
            .options(selectinload(models.Movie.reviews).joinedload(models.Review.user))
            .where(models.Movie.id == id_entity.id)
        )

        async with self._scoped_session_factory() as session:
            if (movie := await session.scalar(stmt)) is not None:
                return [review.to_review_for_movie_entity() for review in movie.reviews]
            raise usecases.interfaces.repositories.movie_errors.MovieNotFoundError
