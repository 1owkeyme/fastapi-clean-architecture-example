from fastapi import APIRouter

from infrastructure.api_servers import responses

from . import dependencies, schemas


router = APIRouter()


@router.post("/")
async def create(
    create_movie_usecase: dependencies.CreateMovieUsecaseDependency,
    create_movie_schema: schemas.movie.CreateMovieSchema,
) -> responses.EmptyResponse:
    movie_info_entity = create_movie_schema.to_movie_info_entity()

    await create_movie_usecase.execute(movie_info=movie_info_entity)

    return responses.EmptyResponse.new()


@router.delete("/")
async def delete(
    delete_movie_usecase: dependencies.DeleteMovieUsecaseDependency,
    delete_movie_schema: schemas.movie.DeleteMovieSchema,
) -> responses.EmptyResponse:
    movie_id_enitity = delete_movie_schema.to_movie_id_entity()

    await delete_movie_usecase.execute(movie_id=movie_id_enitity)

    return responses.EmptyResponse.new()
