from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload

from domain import entities, usecases

from . import models
from .base import AlchemyBaseRepository


class AlchemyUserRepository(AlchemyBaseRepository, usecases.interfaces.repositories.UserRepository):
    def __init__(self, url: str, echo: bool = False) -> None:
        self._scoped_session_factory = self._get_scoped_session_factory(url, echo)

    async def get_user_by_id(self, id_entity: entities.Id) -> entities.user.UserPublic:
        async with self._scoped_session_factory() as session:
            if (user := await session.get(models.User, id_entity.id)) is not None:
                return user.to_user_public_entity()
            raise usecases.interfaces.repositories.user_errors.UserNotFoundError

    async def get_user_private_by_id(self, id_entity: entities.Id) -> entities.user.UserPrivate:
        id_model = models.Id.id_from_entity(id_entity)
        stmt = select(models.User).where(models.User.id == id_model.id)
        async with self._scoped_session_factory() as session:
            if (user := await session.scalar(stmt)) is not None:
                return user.to_user_private_entity()
            raise usecases.interfaces.repositories.user_errors.UserNotFoundError

    async def get_user_private_by_username(self, username_entity: entities.user.Username) -> entities.user.UserPrivate:
        username_model = models.user.Username.username_from_entity(username_entity)

        stmt = select(models.User).where(models.User.username == username_model.username)
        async with self._scoped_session_factory() as session:
            if (user := await session.scalar(stmt)) is not None:
                return user.to_user_private_entity()
            raise usecases.interfaces.repositories.user_errors.UserNotFoundError

    async def get_all_users(self) -> list[entities.user.UserPublic]:
        stmt = select(models.User).order_by(models.User.id)
        async with self._scoped_session_factory() as session:
            users = (await session.scalars(stmt)).all()

        return [user.to_user_public_entity() for user in users]

    async def create_user(self, safe_credentials_entity: entities.user.SafeCredentials) -> entities.Id:
        user = models.User(
            username=safe_credentials_entity.username,
            hashed_password_hex=safe_credentials_entity.hashed_password_hex,
        )
        async with self._scoped_session_factory() as session:
            session.add(user)
            try:
                await session.commit()
            except IntegrityError:
                raise usecases.interfaces.repositories.user_errors.UserAlreadyExistsError from None

        return user.to_user_id_entity()

    async def delete_user_by_id(self, id_entity: entities.Id) -> entities.Id:
        async with self._scoped_session_factory() as session:
            if (user := await session.get(models.User, id_entity.id)) is not None:
                await session.delete(user)
            else:
                raise usecases.interfaces.repositories.user_errors.UserNotFoundError
            await session.commit()
        return id_entity

    async def get_all_user_reviews_by_id(self, id_entity: entities.Id) -> list[entities.review.ReviewForUser]:
        stmt = select(models.User).options(selectinload(models.User.reviews)).where(models.User.id == id_entity.id)
        async with self._scoped_session_factory() as session:
            if (user := await session.scalar(stmt)) is not None:
                return [review.to_review_for_user_entity() for review in user.reviews]
            raise usecases.interfaces.repositories.user_errors.UserNotFoundError
