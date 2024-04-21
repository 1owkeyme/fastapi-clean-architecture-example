from fastapi import APIRouter

from infrastructure.api_servers import responses

from . import dependencies, schemas


router = APIRouter()


@router.post("/sign-up")
async def sign_up(
    sign_up_usecase: dependencies.SignUpUsecaseDependency,
    user_sign_up_schema: schemas.auth.SignUpUserSchema,
) -> responses.EmptyResponse:
    user_credentials_entity = user_sign_up_schema.to_user_credentials_entity()

    await sign_up_usecase.execute(user_credentials=user_credentials_entity)

    return responses.EmptyResponse.new()
