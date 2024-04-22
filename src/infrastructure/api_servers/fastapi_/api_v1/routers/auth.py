from fastapi import APIRouter

from domain import usecases

from . import dependencies, schemas, views


router = APIRouter()


@router.post("/login")
async def login(
    form_data: dependencies.auth.OAuth2PasswordRequestFormDependency,
    authenticate_user_usecase: dependencies.usecases.AuthenticateUserUsecaseDependency,
    create_user_access_token_usecase: dependencies.usecases.CreateUserAccessTokenUsecaseDependency,
) -> views.responses.LoginResponse:
    user_credentials = schemas.users.UserCredentialsSchema.from_oauth2_password_request_form_data(form_data)

    try:
        user_entity = await authenticate_user_usecase.execute(user_credentials.to_user_plain_credentials_entity())
    except usecases.user.interfaces.errors.InvalidCredentialsError:
        # TODO:
        return "ABOBA"

    access_token_entity = await create_user_access_token_usecase.execute(user_entity)

    token_info = views.auth.TokenInfo.from_access_token_entity(access_token_entity)

    return views.responses.LoginResponse.new(token_info=token_info)
