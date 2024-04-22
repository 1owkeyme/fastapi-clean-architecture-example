import typing as t

from fastapi import APIRouter, Path

from . import dependencies, schemas, views


router = APIRouter()


@router.get("/")
async def get_all(
    get_all_users_usecase: dependencies.GetAllUsersUsecaseDependency,
) -> views.responses.GetAllUsersResponse:
    user_public_entities = await get_all_users_usecase.execute()

    users = [
        views.users.UserPublic.from_user_public_entity(user_public_entity)
        for user_public_entity in user_public_entities
    ]

    return views.responses.GetAllUsersResponse.new(users=users)


@router.post("/")
async def create_user(
    create_user_usecase: dependencies.CreateUserUsecaseDependency,
    create_user_schema: schemas.auth.CreateUserSchema,
) -> views.responses.CreateUserResponse:
    user_plain_credentials_entity = create_user_schema.to_user_plain_credentials_entity()

    user_id_entity = await create_user_usecase.execute(
        user_plain_credentials=user_plain_credentials_entity,
    )

    user_id = views.users.UserId.from_user_id_entity(user_id_entity)
    return views.responses.CreateUserResponse.new(user_id=user_id)


@router.get("/{id}/all-reviews")
async def get_all_reviews(
    get_all_user_reviews_usecase: dependencies.GetAllUserReviewsUsecaseDependency,
    id_: t.Annotated[int, Path(alias="id", gt=0)],
) -> views.responses.CreateUserResponse:
    user_id_entity = views.users.UserId(id=id_).to_entity()

    review_enities = await get_all_user_reviews_usecase.execute(user_id_entity)

    

    user_id = views.users.UserId.from_user_id_entity(user_id_entity)
    return views.responses.CreateUserResponse.new(user_id=user_id)
