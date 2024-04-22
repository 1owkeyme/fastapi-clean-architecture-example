import typing as t

from fastapi import APIRouter, Path

from infrastructure.api_servers import responses

from . import dependencies, schemas, views


router = APIRouter()


@router.get("/")
async def get_all_movies(
    get_all_users_usecase: dependencies.usecases.GetAllUsersUsecaseDependency,
) -> views.responses.GetAllUsersResponse:
    user_public_entities = await get_all_users_usecase.execute()

    users = [views.users.UserPublic.from_entity(user_public_entity) for user_public_entity in user_public_entities]

    return views.responses.GetAllUsersResponse.new(users=users)


@router.get("/{id}")
async def get_movie_by_id(
    get_all_users_usecase: dependencies.usecases.GetAllUsersUsecaseDependency,
    id_: t.Annotated[int, Path(alias="id", gt=0)],
) -> views.responses.GetAllUsersResponse:
    user_public_entities = await get_all_users_usecase.execute()

    users = [views.users.UserPublic.from_entity(user_public_entity) for user_public_entity in user_public_entities]

    return views.responses.GetAllUsersResponse.new(users=users)


@router.post("/")
async def create_movie(
    create_movie_usecase: dependencies.usecases.CreateMovieUsecaseDependency,
    create_movie_schema: schemas.movies.CreateMovieSchema,
) -> responses.EmptyResponse:
    movie_info_entity = create_movie_schema.to_movie_info_entity()

    await create_movie_usecase.execute(movie_info=movie_info_entity)

    return responses.EmptyResponse.new()


@router.delete("/")
async def delete_movie(
    delete_movie_usecase: dependencies.usecases.DeleteMovieUsecaseDependency,
    delete_movie_schema: schemas.movies.DeleteMovieSchema,
) -> responses.EmptyResponse:
    movie_id_enitity = delete_movie_schema.to_movie_id_entity()

    await delete_movie_usecase.execute(movie_id=movie_id_enitity)

    return responses.EmptyResponse.new()


@router.get("/{id}/reviews")
async def get_all_movie_reviews(
    get_all_user_reviews_usecase: dependencies.usecases.GetAllUserReviewsUsecaseDependency,
    id_: t.Annotated[int, Path(alias="id", gt=0)],
) -> views.responses.CreateUserResponse:
    return views.responses.CreateUserResponse.new(user_id=user_id)
