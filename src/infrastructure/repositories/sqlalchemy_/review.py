from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload

from domain import entities, usecases

from . import models
from .base import AlchemyBaseRepository


class AlchemyReviewRepository(AlchemyBaseRepository, usecases.interfaces.repositories.ReviewRepository):
    def __init__(self, url: str, echo: bool = False) -> None:
        self._scoped_session_factory = self._get_scoped_session_factory(url, echo)

    async def get_review_by_id(self, id_entity: entities.Id) -> entities.review.Review:
        stmt = (
            select(models.Review)
            .options(joinedload(models.Review.user), joinedload(models.Review.movie))
            .where(models.Review.id == id_entity.id)
        )
        async with self._scoped_session_factory() as session:
            if (review := await session.scalar(stmt)) is not None:
                return review.to_entity()
            raise usecases.interfaces.repositories.review_errors.ReviewNotFoundError

    async def create_review_by_movie_id(
        self,
        user_id_entity: entities.Id,
        movie_id_entity: entities.Id,
        info_entity: entities.review.ReviewInfo,
    ) -> entities.Id:
        review_info = models.review.ReviewInfo.review_info_from_entity(info_entity)
        user_id = models.Id.id_from_entity(user_id_entity)
        movie_id = models.Id.id_from_entity(movie_id_entity)

        review = models.Review(
            user_id=user_id.id,
            movie_id=movie_id.id,
            stars_10x=review_info.stars_10x,
            text=review_info.text,
        )
        async with self._scoped_session_factory() as session:
            session.add(review)
            try:
                await session.commit()
            except IntegrityError:
                raise usecases.interfaces.repositories.review_errors.ReviewAlreadyExistsError from None

        return review.to_id_entity()

    async def delete_review_by_id(self, id_entity: entities.Id) -> entities.Id:
        async with self._scoped_session_factory() as session:
            if (review := await session.get(models.Review, id_entity.id)) is not None:
                await session.delete(review)
            else:
                raise usecases.interfaces.repositories.review_errors.ReviewNotFoundError
            await session.commit()
        return id_entity
