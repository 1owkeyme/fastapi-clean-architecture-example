from fastapi import APIRouter

from . import dependencies, schemas, views


router = APIRouter()


@router.get("/")
async def get_all_users(
    get_all_users_usecase: dependencies.usecases.GetAllUsersUsecaseDependency,
) -> views.responses.GetAllUsersResponse:
    user_public_entities = await get_all_users_usecase.execute()

    users = [views.users.UserPublic.from_entity(user_public_entity) for user_public_entity in user_public_entities]

    return views.responses.GetAllUsersResponse.new(users=users)


@router.get("/{id}")
async def get_user_by_id(
    get_user_by_id_usecase: dependencies.usecases.GetUserByIdUsecaseDependency,
    user_id: dependencies.path.UserIdFromPathDependency,
) -> views.responses.GetUserByIdResponse:
    user_id_entity = user_id.to_entity()

    user_enitity = await get_user_by_id_usecase.execute(user_id_entity)

    user = views.users.UserPublic.from_entity(user_enitity)

    return views.responses.GetUserByIdResponse.new(user=user)


@router.post("/")
async def create_user(
    create_user_usecase: dependencies.usecases.CreateUserUsecaseDependency,
    create_user_schema: schemas.users.CreateUserSchema,
) -> views.responses.CreateUserResponse:
    user_plain_credentials_entity = create_user_schema.to_user_plain_credentials_entity()

    user_id_entity = await create_user_usecase.execute(
        user_plain_credentials=user_plain_credentials_entity,
    )

    user_id = views.users.UserId.from_user_id_entity(user_id_entity)
    return views.responses.CreateUserResponse.new(user_id=user_id)


@router.delete("/")
async def delete_user(
    create_user_usecase: dependencies.usecases.CreateUserUsecaseDependency,
    create_user_schema: schemas.users.CreateUserSchema,
) -> views.responses.CreateUserResponse:
    user_plain_credentials_entity = create_user_schema.to_user_plain_credentials_entity()

    user_id_entity = await create_user_usecase.execute(
        user_plain_credentials=user_plain_credentials_entity,
    )

    user_id = views.users.UserId.from_user_id_entity(user_id_entity)
    return views.responses.CreateUserResponse.new(user_id=user_id)


@router.get("/{id}/reviews")
async def get_all_user_reviews(
    get_all_user_reviews_usecase: dependencies.usecases.GetAllUserReviewsUsecaseDependency,
    user_id: dependencies.path.UserIdFromPathDependency,
) -> views.responses.GetAllUserReviewsResponse:
    user_id_entity = user_id.to_entity()

    review_for_user_entities = await get_all_user_reviews_usecase.execute(user_id_entity)

    reviews_for_user = [
        views.reviews.ReviewForUser.from_entity(review_for_user_entity)
        for review_for_user_entity in review_for_user_entities
    ]
    return views.responses.GetAllUserReviewsResponse.new(reviews_for_user=reviews_for_user)
