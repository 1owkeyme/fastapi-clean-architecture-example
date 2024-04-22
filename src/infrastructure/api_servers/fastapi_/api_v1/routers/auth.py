from api_servers import responses
from fastapi import APIRouter

from domain import usecases

from . import dependencies, schemas


router = APIRouter()


@router.post("/login")
async def login(
    form_Data: dependencies.auth.OAuth2PasswordRequestFormDependency,
    authenticate_user_usecase: dependencies.usecases.AuthenticateUserUsecaseDependency,
) -> responses.EmptyResponse:
    user_credentials = schemas.users.UserCredentialsSchema.from_oauth2_password_request_form_data(form_Data)

    try:
        user = await authenticate_user_usecase.execute(user_credentials.to_user_plain_credentials_entity())
    except usecases.user.interfaces.errors.InvalidCredentialsError:
        # TODO:
        return "ABOBA"

    return responses.EmptyResponse.new()
