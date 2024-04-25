import typing as t
from http import HTTPStatus

from fastapi import Depends, HTTPException

from domain import usecases


review_usecases_builder: usecases.review.ReviewUsecasesBuilder | None = None


def __get_review_usecases_builder() -> usecases.review.ReviewUsecasesBuilder:
    if review_usecases_builder is None:
        raise HTTPException(status_code=HTTPStatus.SERVICE_UNAVAILABLE, detail="Usecases are not initialized")
    return review_usecases_builder


def __get_get_review_by_id_usecase() -> usecases.review.GetReviewByIdUsecase:
    return __get_review_usecases_builder().construct_get_review_by_id_usecase()


GetReviewByIdUsecaseDependency = t.Annotated[
    usecases.review.GetReviewByIdUsecase, Depends(__get_get_review_by_id_usecase)
]


def __get_create_review_by_movie_id_usecase() -> usecases.review.CreateReviewByMovieIdUsecase:
    return __get_review_usecases_builder().construct_create_review_by_movie_id_usecase()


CreateReviewByMovieIdUsecaseDependency = t.Annotated[
    usecases.review.CreateReviewByMovieIdUsecase, Depends(__get_create_review_by_movie_id_usecase)
]


def __get_delete_review_by_id_usecase() -> usecases.review.DeleteReviewByIdUsecase:
    return __get_review_usecases_builder().construct_delete_review_by_id_usecase()


DeleteReviewByIdUsecaseDependency = t.Annotated[
    usecases.review.DeleteReviewByIdUsecase, Depends(__get_delete_review_by_id_usecase)
]
