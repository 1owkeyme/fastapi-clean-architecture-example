import typing as t

from fastapi import Depends

from domain import usecases


movie_usecases_builder: usecases.movie.MovieUsecasesBuilder | None = None


def __get_movie_usecases_builder() -> usecases.movie.MovieUsecasesBuilder:
    if movie_usecases_builder is None:
        raise RuntimeError  # TODO: raise HTTPException or smth
    return movie_usecases_builder


def __get_create_movie_usecase() -> usecases.movie.CreateMovieUsecase:
    return __get_movie_usecases_builder().construct_create_movie_usecase()


CreateMovieUsecaseDependency = t.Annotated[usecases.movie.CreateMovieUsecase, Depends(__get_create_movie_usecase)]


def __get_delete_movie_by_id_usecase() -> usecases.movie.DeleteMovieByIdUsecase:
    return __get_movie_usecases_builder().construct_delete_movie_by_id_usecase()


DeleteMovieByIdUsecaseDependency = t.Annotated[
    usecases.movie.DeleteMovieByIdUsecase, Depends(__get_delete_movie_by_id_usecase)
]


def __get_get_all_movie_reviews_by_id_usecase() -> usecases.movie.GetAllMovieReviewsByIdUsecase:
    return __get_movie_usecases_builder().construct_get_all_movie_reviews_by_id_usecase()


GetAllMovieReviewsByIdUsecaseDependency = t.Annotated[
    usecases.movie.GetAllMovieReviewsByIdUsecase, Depends(__get_get_all_movie_reviews_by_id_usecase)
]


def __get_get_all_movies_usecase() -> usecases.movie.GetAllMoviesUsecase:
    return __get_movie_usecases_builder().construct_get_all_movies_usecase()


GetAllMoviesUsecaseDependency = t.Annotated[usecases.movie.GetAllMoviesUsecase, Depends(__get_get_all_movies_usecase)]


def __get_get_movie_by_id_usecase() -> usecases.movie.GetMovieByIdUsecase:
    return __get_movie_usecases_builder().construct_get_movie_by_id_usecase()


GetMovieByIdUsecaseDependency = t.Annotated[usecases.movie.GetMovieByIdUsecase, Depends(__get_get_movie_by_id_usecase)]
