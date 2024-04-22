import typing as t

from fastapi import APIRouter, Path

from . import dependencies, schemas, views


router = APIRouter()


@router.get("/{id}")
async def get_review_by_id(
    get_all_users_usecase: dependencies.usecases.GetAllUsersUsecaseDependency,
    id_: t.Annotated[int, Path(alias="id", gt=0)],
) -> views.responses.GetAllUsersResponse:
    user_public_entities = await get_all_users_usecase.execute()

    users = [
        views.users.UserPublic.from_user_public_entity(user_public_entity)
        for user_public_entity in user_public_entities
    ]

    return views.responses.GetAllUsersResponse.new(users=users)


@router.post("/")
async def create_review(
    create_review_usecase: dependencies.usecases.CreateReviewUsecaseDependency,
    create_review_schema: schemas.reviews.CreateReviewSchema,
) -> views.responses.CreateUserResponse:
    user_plain_credentials_entity = create_user_schema.to_user_plain_credentials_entity()

    user_id_entity = await create_user_usecase.execute(
        user_plain_credentials=user_plain_credentials_entity,
    )

    user_id = views.users.UserId.from_user_id_entity(user_id_entity)
    return views.responses.CreateUserResponse.new(user_id=user_id)


@router.delete("/")
async def delete_review(
    create_user_usecase: dependencies.usecases.CreateUserUsecaseDependency,
    create_user_schema: schemas.users.CreateUserSchema,
) -> views.responses.CreateUserResponse:
    user_plain_credentials_entity = create_user_schema.to_user_plain_credentials_entity()

    user_id_entity = await create_user_usecase.execute(
        user_plain_credentials=user_plain_credentials_entity,
    )

    user_id = views.users.UserId.from_user_id_entity(user_id_entity)
    return views.responses.CreateUserResponse.new(user_id=user_id)
