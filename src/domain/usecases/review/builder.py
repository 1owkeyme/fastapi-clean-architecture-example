from .. import interfaces
from .create import CreateReviewByMovieIdUsecase
from .delete_by_id import DeleteReviewByIdUsecase
from .get_by_id import GetReviewByIdUsecase


class ReviewUsecasesBuilder:
    def __init__(self, review_repository: interfaces.repositories.ReviewRepository) -> None:
        self._review_repository = review_repository

    def construct_get_review_by_id_usecase(self) -> GetReviewByIdUsecase:
        return GetReviewByIdUsecase(review_repository=self._review_repository)

    def construct_create_review_by_movie_id_usecase(self) -> CreateReviewByMovieIdUsecase:
        return CreateReviewByMovieIdUsecase(review_repository=self._review_repository)

    def construct_delete_review_by_id_usecase(self) -> DeleteReviewByIdUsecase:
        return DeleteReviewByIdUsecase(review_repository=self._review_repository)
