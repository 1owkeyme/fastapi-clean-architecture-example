from . import interfaces
from .create import CreateReviewUsecase
from .delete import DeleteReviewUsecase


class ReviewUsecasesBuilder:
    def __init__(self, review_repository: interfaces.ReviewRepository) -> None:
        self._review_repository = review_repository

    def construct_create_review_usecase(self) -> CreateReviewUsecase:
        return CreateReviewUsecase(review_repository=self._review_repository)

    def construct_delete_review_usecase(self) -> DeleteReviewUsecase:
        return DeleteReviewUsecase(review_repository=self._review_repository)
