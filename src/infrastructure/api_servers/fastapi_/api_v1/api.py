from fastapi import APIRouter

from domain import usecases

from .routers import auth, dependencies, movies


def get_api_router(
    auth_usecases_builder: usecases.auth.AuthUsecasesBuilder,
    movie_usecases_builder: usecases.movie.MovieUsecasesBuilder,
) -> APIRouter:
    dependencies.auth_usecases_builder = auth_usecases_builder
    dependencies.movie_usecases_builder = movie_usecases_builder

    router = APIRouter()

    router.include_router(auth.router, prefix="/auth", tags=["auth"])
    router.include_router(movies.router, prefix="/users", tags=["users"])

    return router
