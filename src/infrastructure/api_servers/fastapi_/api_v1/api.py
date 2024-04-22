from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer

from domain import usecases

from .routers import auth, dependencies, movies, reviews, users


def get_api_router(
    user_usecases_builder: usecases.user.UserUsecasesBuilder,
    movie_usecases_builder: usecases.movie.MovieUsecasesBuilder,
    review_usecases_builder: usecases.review.ReviewUsecasesBuilder,
    reusable_oauth2: OAuth2PasswordBearer,
) -> APIRouter:
    dependencies.usecases.user_usecases_builder = user_usecases_builder
    dependencies.usecases.movie_usecases_builder = movie_usecases_builder
    dependencies.usecases.review_usecases_builder = review_usecases_builder

    dependencies.auth.reusable_oauth2 = reusable_oauth2

    router = APIRouter()

    router.include_router(auth.router, prefix="/auth", tags=["auth"])
    router.include_router(users.router, prefix="/users", tags=["users"])
    router.include_router(movies.router, prefix="/movies", tags=["movies"])
    router.include_router(reviews.router, prefix="/reviews", tags=["reviews"])

    return router
