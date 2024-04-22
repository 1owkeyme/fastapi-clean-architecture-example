from domain import entities

from . import interfaces


class GetAllUserReviewsUsecase:
    def __init__(self, user_repository: interfaces.UserRepository) -> None:
        self._user_repository = user_repository

    async def execute(self, user_id: entities.user.UserId) -> list[entities.review.Review]:
        return await self._user_repository.get_all_user_reviews(id_entity=user_id)
