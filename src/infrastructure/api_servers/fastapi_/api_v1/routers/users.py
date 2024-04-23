from fastapi import APIRouter

from . import dependencies, schemas, views


router = APIRouter()


@router.get("/", dependencies=[dependencies.auth.EnsureCurrentSuperUserIdDependency])
async def get_all_users(
    get_all_users_usecase: dependencies.usecases.GetAllUsersUsecaseDependency,
) -> views.responses.user.GetAllUsersResponse:
    user_public_entities = await get_all_users_usecase.execute()

    users = [views.users.UserPublic.from_entity(user_public_entity) for user_public_entity in user_public_entities]

    return views.responses.user.GetAllUsersResponse.new(users=users)


@router.get("/{user_id}", dependencies=[dependencies.auth.EnsureCurrentSuperUserIdDependency])
async def get_user_by_id(
    get_user_by_id_usecase: dependencies.usecases.GetUserByIdUsecaseDependency,
    user_id: dependencies.path.UserIdFromPathDependency,
) -> views.responses.user.GetUserByIdResponse:
    user_id_entity = user_id.to_entity()

    user_enitity = await get_user_by_id_usecase.execute(user_id_entity)

    user = views.users.UserPublic.from_entity(user_enitity)

    return views.responses.user.GetUserByIdResponse.new(user=user)


@router.post("/", dependencies=[dependencies.auth.EnsureCurrentSuperUserIdDependency])
async def create_user(
    create_user_usecase: dependencies.usecases.CreateUserUsecaseDependency,
    create_user_schema: schemas.users.CreateUserSchema,
) -> views.responses.user.CreateUserResponse:
    user_plain_credentials_entity = create_user_schema.to_user_plain_credentials_entity()

    user_id_entity = await create_user_usecase.execute(
        user_plain_credentials=user_plain_credentials_entity,
    )

    user_id = views.users.UserId.from_user_id_entity(user_id_entity)
    return views.responses.user.CreateUserResponse.new(user_id=user_id)


@router.delete("/{user_id}", dependencies=[dependencies.auth.EnsureCurrentSuperUserIdDependency])
async def delete_user_by_id(
    create_user_usecase: dependencies.usecases.CreateUserUsecaseDependency,
    user_id: dependencies.path.UserIdFromPathDependency,
) -> views.responses.user.CreateUserResponse: ...


@router.get("/{user_id}/reviews", dependencies=[dependencies.auth.EnsureCurrentUserIdDependency])
async def get_all_user_reviews(
    get_all_user_reviews_usecase: dependencies.usecases.GetAllUserReviewsUsecaseDependency,
    user_id: dependencies.path.UserIdFromPathDependency,
) -> views.responses.user.GetAllUserReviewsResponse:
    user_id_entity = user_id.to_entity()

    review_for_user_entities = await get_all_user_reviews_usecase.execute(user_id_entity)

    reviews_for_user = [
        views.reviews.ReviewForUser.from_entity(review_for_user_entity)
        for review_for_user_entity in review_for_user_entities
    ]
    return views.responses.user.GetAllUserReviewsResponse.new(reviews_for_user=reviews_for_user)
