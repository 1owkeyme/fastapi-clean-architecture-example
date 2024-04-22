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


def __get_create_user_usecase() -> usecases.user.CreateUserUsecase:
    return __get_user_usecases_builder().construct_create_user_usecase()


CreateUserUsecaseDependency = t.Annotated[usecases.user.CreateUserUsecase, Depends(__get_create_user_usecase)]


def __get_delete_user_usecase() -> usecases.user.DeleteUserUsecase:
    return __get_user_usecases_builder().construct_delete_user_usecase()


DeleteUserUsecaseDependency = t.Annotated[usecases.user.DeleteUserUsecase, Depends(__get_delete_user_usecase)]


def __get_get_all_users_usecase() -> usecases.user.GetAllUsersUsecase:
    return __get_user_usecases_builder().construct_get_all_users_usecase()


GetAllUsersUsecaseDependency = t.Annotated[usecases.user.GetAllUsersUsecase, Depends(__get_get_all_users_usecase)]


def __get_get_all_user_reviews_usecase() -> usecases.user.GetAllUserReviewsUsecase:
    return __get_user_usecases_builder().construct_get_all_user_reviews_usecase()


GetAllUserReviewsUsecaseDependency = t.Annotated[
    usecases.user.GetAllUserReviewsUsecase, Depends(__get_get_all_user_reviews_usecase)
]


def __get_get_user_by_id_usecase() -> usecases.user.GetUserByIdUsecase:
    return __get_user_usecases_builder().construct_get_user_by_id_usecase()


GetUserByIdUsecaseDependency = t.Annotated[usecases.user.GetUserByIdUsecase, Depends(__get_get_user_by_id_usecase)]


def __get_authenticate_user_usecase() -> usecases.user.AuthenticateUserUsecase:
    return __get_user_usecases_builder().construct_authenticate_user_usecase()


AuthenticateUserUsecaseDependency = t.Annotated[
    usecases.user.AuthenticateUserUsecase, Depends(__get_authenticate_user_usecase)
]


def __get_create_user_access_token_usecase() -> usecases.user.CreateUserAccessTokenUsecase:
    return __get_user_usecases_builder().construct_create_user_access_token_usecase()


CreateUserAccessTokenUsecaseDependency = t.Annotated[
    usecases.user.CreateUserAccessTokenUsecase, Depends(__get_create_user_access_token_usecase)
]


def __get_read_user_access_token_usecase() -> usecases.user.ReadUserAccessTokenUsecase:
    return __get_user_usecases_builder().construct_read_user_access_token_usecase()


ReadUserAccessTokenUsecaseDependency = t.Annotated[
    usecases.user.ReadUserAccessTokenUsecase, Depends(__get_read_user_access_token_usecase)
]


def __get_is_user_super_user_usecase() -> usecases.user.IsUserSuperUserUsecase:
    return __get_user_usecases_builder().construct_is_user_super_user_usecase()


IsUserSuperUserUsecaseDependency = t.Annotated[
    usecases.user.IsUserSuperUserUsecase, Depends(__get_is_user_super_user_usecase)
]


def __get_create_movie_usecase() -> usecases.movie.CreateMovieUsecase:
    return __get_movie_usecases_builder().construct_create_movie_usecase()


CreateMovieUsecaseDependency = t.Annotated[usecases.movie.CreateMovieUsecase, Depends(__get_create_movie_usecase)]


def __get_delete_movie_usecase() -> usecases.movie.DeleteMovieUsecase:
    return __get_movie_usecases_builder().construct_delete_movie_usecase()


DeleteMovieUsecaseDependency = t.Annotated[usecases.movie.DeleteMovieUsecase, Depends(__get_delete_movie_usecase)]


def __get_get_all_movie_reviews_usecase() -> usecases.movie.GetAllMovieReviewsUsecase:
    return __get_movie_usecases_builder().construct_get_all_movie_reviews_usecase()


GetAllMovieReviewsUsecaseDependency = t.Annotated[
    usecases.movie.GetAllMovieReviewsUsecase, Depends(__get_get_all_movie_reviews_usecase)
]


def __get_get_all_movies_usecase() -> usecases.movie.GetAllMoviesUsecase:
    return __get_movie_usecases_builder().construct_get_all_movies_usecase()


GetAllMoviesUsecaseDependency = t.Annotated[usecases.movie.GetAllMoviesUsecase, Depends(__get_get_all_movies_usecase)]


def __get_get_movie_by_id_usecase() -> usecases.movie.GetMovieByIdUsecase:
    return __get_movie_usecases_builder().construct_get_movie_by_id_usecase()


GetMovieByIdUsecaseDependency = t.Annotated[usecases.movie.GetMovieByIdUsecase, Depends(__get_get_movie_by_id_usecase)]


def __get_create_review_usecase() -> usecases.review.CreateReviewUsecase:
    return __get_review_usecases_builder().construct_create_review_usecase()


CreateReviewUsecaseDependency = t.Annotated[usecases.review.CreateReviewUsecase, Depends(__get_create_review_usecase)]


def __get_delete_review_usecase() -> usecases.review.DeleteReviewUsecase:
    return __get_review_usecases_builder().construct_delete_review_usecase()


DeleteReviewUsecaseDependency = t.Annotated[usecases.review.DeleteReviewUsecase, Depends(__get_delete_review_usecase)]
