from fastapi import APIRouter

from domain import usecases

from .routers import auth, dependencies, users


def get_api_router(
    auth_usecases_builder: usecases.auth.AuthUsecasesBuilder,
) -> APIRouter:
    dependencies.auth_usecases_builder = auth_usecases_builder

    router = APIRouter()

    router.include_router(auth.router, prefix="/auth", tags=["auth"])
    router.include_router(users.router, prefix="/users", tags=["users"])

    return router
