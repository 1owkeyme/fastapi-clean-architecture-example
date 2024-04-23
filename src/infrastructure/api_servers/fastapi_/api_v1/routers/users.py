from fastapi import APIRouter

from . import dependencies, responses, schemas


router = APIRouter()


@router.get("/", dependencies=[dependencies.auth.EnsureCurrentSuperUserIdDependency])
async def get_all_users(
    get_all_users_usecase: dependencies.usecases.user.GetAllUsersUsecaseDependency,
) -> responses.user.GetAllUsersResponse:
    user_public_entities = await get_all_users_usecase.execute()

    users = [schemas.user.UserPublic.from_entity(user_public_entity) for user_public_entity in user_public_entities]

    return responses.user.GetAllUsersResponse.new(users=users)


@router.get("/{user_id}", dependencies=[dependencies.auth.EnsureCurrentSuperUserIdDependency])
async def get_user_by_id(
    get_user_by_id_usecase: dependencies.usecases.user.GetUserByIdUsecaseDependency,
    user_id: dependencies.path.UserIdFromPathDependency,
) -> responses.user.GetUserByIdResponse:
    user_id_entity = user_id.to_id_entity()

    user_enitity = await get_user_by_id_usecase.execute(user_id_entity)

    user = schemas.user.UserPublic.from_entity(user_enitity)
    return responses.user.GetUserByIdResponse.new(user=user)


@router.post("/", dependencies=[dependencies.auth.EnsureCurrentSuperUserIdDependency])
async def create_user(
    create_user_usecase: dependencies.usecases.user.CreateUserUsecaseDependency,
    create_user_schema: schemas.user.CreateUser,
) -> responses.user.CreateUserResponse:
    user_plain_credentials_entity = create_user_schema.to_user_plain_credentials_entity()

    user_id_entity = await create_user_usecase.execute(
        user_plain_credentials=user_plain_credentials_entity,
    )

    user_id_schema = schemas.user.UserId.from_id_entity(user_id_entity)
    return responses.user.CreateUserResponse.new(id_=user_id_schema.user_id)


@router.delete("/{user_id}", dependencies=[dependencies.auth.EnsureCurrentSuperUserIdDependency])
async def delete_user_by_id(
    delete_user_usecase: dependencies.usecases.user.DeleteUserByIdUsecaseDependency,
    user_id: dependencies.path.UserIdFromPathDependency,
) -> responses.user.DeleteUserByIdResponse:
    deleted_user_id_entity = await delete_user_usecase.execute(user_id=user_id.to_id_entity())

    user_id_schema = schemas.user.UserId.from_id_entity(deleted_user_id_entity)

    return responses.user.DeleteUserByIdResponse.new(id_=user_id_schema.user_id)


@router.get("/{user_id}/reviews", dependencies=[dependencies.auth.EnsureCurrentUserIdDependency])
async def get_all_user_reviews_by_id(
    get_all_user_reviews_usecase: dependencies.usecases.user.GetAllUserReviewsByIdUsecaseDependency,
    user_id: dependencies.path.UserIdFromPathDependency,
) -> responses.user.GetAllUserReviewsByIdResponse:
    user_id_entity = user_id.to_id_entity()

    review_for_user_entities = await get_all_user_reviews_usecase.execute(user_id_entity)

    reviews_for_user = [
        schemas.review.ReviewForUser.from_entity(review_for_user_entity)
        for review_for_user_entity in review_for_user_entities
    ]
    return responses.user.GetAllUserReviewsByIdResponse.new(reviews_for_user=reviews_for_user)
