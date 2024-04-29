from fastapi import APIRouter

from domain import usecases

from . import dependencies, responses, schemas


router = APIRouter()


@router.post("/login")
async def login(
    user_credentials_form: dependencies.forms.UserCredentialFormDependency,
    authenticate_user_usecase: dependencies.usecases.auth.AuthenticateUserUsecaseDependency,
    create_user_access_token_usecase: dependencies.usecases.auth.CreateUserAccessTokenUsecaseDependency,
) -> responses.auth.LoginResponse | responses.auth.InvalidCredentialsResponse:
    try:
        user_entity = await authenticate_user_usecase.execute(user_credentials_form.to_user_plain_credentials_entity())
    except usecases.auth.errors.InvalidCredentialsError:
        return responses.auth.InvalidCredentialsResponse.new()
    access_token_entity = await create_user_access_token_usecase.execute(user_entity)

    return schemas.auth.TokenInfo.from_access_token_entity(access_token_entity)
