from fastapi import APIRouter

from domain import usecases

from . import dependencies, responses, schemas


router = APIRouter()


@router.get("/", dependencies=[dependencies.auth.EnsureCurrentUserDependency])
async def get_all_movies(
    get_all_movies_usecase: dependencies.usecases.movie.GetAllMoviesUsecaseDependency,
) -> responses.movie.GetAllMoviesResponse:
    movie_entities = await get_all_movies_usecase.execute()

    movies = [schemas.movie.Movie.from_movie_entity(movie_entity) for movie_entity in movie_entities]

    return responses.movie.GetAllMoviesResponse.new(movies=movies)


@router.get("/{movie_id}", dependencies=[dependencies.auth.EnsureCurrentUserDependency])
async def get_movie_by_id(
    get_movie_by_id_usecase: dependencies.usecases.movie.GetMovieByIdUsecaseDependency,
    movie_id: dependencies.path.MovieIdFromPathDependency,
) -> responses.movie.GetMovieByIdResponse | responses.movie.MovieNotFoundErrorResponse:
    try:
        movie_entity = await get_movie_by_id_usecase.execute(movie_id.to_id_entity())
    except usecases.movie.errors.MovieNotFoundError:
        return responses.movie.MovieNotFoundErrorResponse.new()
    movie = schemas.movie.Movie.from_movie_entity(movie_entity)
    return responses.movie.GetMovieByIdResponse.new(movie=movie)


@router.post("/", dependencies=[dependencies.auth.EnsureCurrentSuperUserDependency])
async def create_movie(
    create_movie_usecase: dependencies.usecases.movie.CreateMovieUsecaseDependency,
    create_movie_schema: schemas.movie.CreateMovie,
) -> responses.movie.CreateMovieResponse | responses.movie.MovieAlreadyExistsErrorResponse:
    movie_info_entity = create_movie_schema.to_movie_info_entity()
    try:
        movie_id_entity = await create_movie_usecase.execute(movie_info=movie_info_entity)
    except usecases.movie.errors.MovieAlreadyExistsError:
        return responses.movie.MovieAlreadyExistsErrorResponse.new()

    id_schema = schemas.Id.from_id_entity(movie_id_entity)

    return responses.movie.CreateMovieResponse.new(id_schema.id)


@router.delete("/{movie_id}", dependencies=[dependencies.auth.EnsureCurrentSuperUserDependency])
async def delete_movie_by_id(
    delete_movie_by_id_usecase: dependencies.usecases.movie.DeleteMovieByIdUsecaseDependency,
    movie_id: dependencies.path.MovieIdFromPathDependency,
) -> responses.movie.DeleteMovieByIdResponse | responses.movie.MovieNotFoundErrorResponse:
    try:
        deleted_movie_id_entity = await delete_movie_by_id_usecase.execute(movie_id=movie_id.to_id_entity())
    except usecases.movie.errors.MovieNotFoundError:
        return responses.movie.MovieNotFoundErrorResponse.new()
    movie_id_schema = schemas.Id.from_id_entity(deleted_movie_id_entity)

    return responses.movie.DeleteMovieByIdResponse.new(movie_id_schema.id)


@router.get(
    "/{movie_id}/reviews",
    dependencies=[dependencies.auth.EnsureCurrentUserDependency],
)
async def get_all_movie_reviews_by_id(
    get_all_movie_reviews_by_id_usecase: dependencies.usecases.movie.GetAllMovieReviewsByIdUsecaseDependency,
    movie_id: dependencies.path.MovieIdFromPathDependency,
) -> responses.movie.GetAllMovieReviewsByIdResponse | responses.movie.MovieNotFoundErrorResponse:
    try:
        review_for_movie_entities = await get_all_movie_reviews_by_id_usecase.execute(movie_id.to_id_entity())
    except usecases.movie.errors.MovieNotFoundError:
        return responses.movie.MovieNotFoundErrorResponse.new()
    reviews_for_movie = [
        schemas.review.ReviewForMovie.from_entity(review_for_movie_entity)
        for review_for_movie_entity in review_for_movie_entities
    ]
    return responses.movie.GetAllMovieReviewsByIdResponse.new(reviews_for_movie=reviews_for_movie)
