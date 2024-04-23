from domain import entities

from .. import interfaces


class GetAllUserReviewsByIdUsecase:
    def __init__(self, user_repository: interfaces.repositories.UserRepository) -> None:
        self._user_repository = user_repository

    async def execute(self, user_id: entities.Id) -> list[entities.review.ReviewForUser]:
        return await self._user_repository.get_all_user_reviews_by_id(id_entity=user_id)
