from fastapi import APIRouter

from infrastructure.api_servers import responses

from . import dependencies, schemas


router = APIRouter()


@router.post("/")
async def create_user(
    create_user_usecase: dependencies.CreateUserUsecaseDependency,
    create_user_schema: schemas.auth.CreateUserSchema,
) -> responses.EmptyResponse:
    user_plain_credentials_entity = (
        create_user_schema.to_user_plain_credentials_entity()
    )

    await create_user_usecase.execute(
        user_plain_credentials=user_plain_credentials_entity,
    )

    return responses.EmptyResponse.new()
