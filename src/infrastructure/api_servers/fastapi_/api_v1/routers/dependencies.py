import typing as t

from fastapi import Depends

from domain import usecases


user_usecases_builder: usecases.user.UserUsecasesBuilder | None = None
movie_usecases_builder: usecases.movie.MovieUsecasesBuilder | None = None
review_usecases_builder: usecases.review.ReviewUsecasesBuilder | None = None


def __get_user_usecases_builder() -> usecases.user.UserUsecasesBuilder:
    if user_usecases_builder is None:
        raise RuntimeError  # TODO: raise HTTPException or smth
    return user_usecases_builder


def __get_movie_usecases_builder() -> usecases.movie.MovieUsecasesBuilder:
    if movie_usecases_builder is None:
        raise RuntimeError  # TODO: raise HTTPException or smth
    return movie_usecases_builder


def __get_review_usecases_builder() -> usecases.review.ReviewUsecasesBuilder:
    if review_usecases_builder is None:
        raise RuntimeError  # TODO: raise HTTPException or smth
    return review_usecases_builder


def __get_sign_in_usecase() -> usecases.user.SignInUsecase:
    return __get_user_usecases_builder().construct_sign_in_usecase()


SignInUsecaseDependency = t.Annotated[
    usecases.user.SignInUsecase, Depends(__get_sign_in_usecase)
]


def __get_sign_up_usecase() -> usecases.user.CreateUserUsecase:
    return __get_user_usecases_builder().construct_sign_up_usecase()


CreateUserUsecaseDependency = t.Annotated[
    usecases.user.CreateUserUsecase, Depends(__get_sign_up_usecase)
]


def __get_create_movie_usecase() -> usecases.movie.CreateMovieUsecase:
    return __get_movie_usecases_builder().construct_create_movie_usecase()


CreateMovieUsecaseDependency = t.Annotated[
    usecases.movie.CreateMovieUsecase, Depends(__get_create_movie_usecase)
]


def __get_delete_movie_usecase() -> usecases.movie.DeleteMovieUsecase:
    return __get_movie_usecases_builder().construct_delete_movie_usecase()


DeleteMovieUsecaseDependency = t.Annotated[
    usecases.movie.DeleteMovieUsecase, Depends(__get_delete_movie_usecase)
]


def __get_create_review_usecase() -> usecases.review.CreateReviewUsecase:
    return __get_review_usecases_builder().construct_create_review_usecase()


CreateReviewUsecaseDependency = t.Annotated[
    usecases.review.CreateReviewUsecase, Depends(__get_create_review_usecase)
]


def __get_delete_review_usecase() -> usecases.review.DeleteReviewUsecase:
    return __get_review_usecases_builder().construct_delete_review_usecase()


DeleteReviewUsecaseDependency = t.Annotated[
    usecases.review.DeleteReviewUsecase, Depends(__get_delete_review_usecase)
]
