from fastapi import APIRouter

from . import dependencies, schemas, views


router = APIRouter()


@router.get("/", dependencies=[dependencies.auth.EnsureCurrentUserIdDependency])
async def get_all_movies(
    get_all_movies_usecase: dependencies.usecases.GetAllMoviesUsecaseDependency,
) -> views.responses.movie.GetAllMoviesResponse:
    movie_entities = await get_all_movies_usecase.execute()

    movies = [views.movie.Movie.from_entity(movie_entity) for movie_entity in movie_entities]

    return views.responses.movie.GetAllMoviesResponse.new(movies=movies)


@router.get("/{id}", dependencies=[dependencies.auth.EnsureCurrentUserIdDependency])
async def get_movie_by_id(
    get_movie_by_id_usecase: dependencies.usecases.GetMovieByIdUsecaseDependency,
    movie_id: dependencies.path.MovieIdFromPathDependency,
) -> views.responses.movie.GetMovieByIdResponse:
    movie_entity = await get_movie_by_id_usecase.execute(movie_id.to_entity())
    movie = views.movie.Movie.from_entity(movie_entity)
    return views.responses.movie.GetMovieByIdResponse.new(movie=movie)


@router.post("/", dependencies=[dependencies.auth.EnsureCurrentSuperUserIdDependency])
async def create_movie(
    create_movie_usecase: dependencies.usecases.CreateMovieUsecaseDependency,
    create_movie_schema: schemas.movies.CreateMovieSchema,
) -> views.responses.movie.CreateMovieResponse:
    movie_info_entity = create_movie_schema.to_movie_info_entity()

    movie_id_entity = await create_movie_usecase.execute(movie_info=movie_info_entity)

    movie_id = views.movie.MovieId.from_entity(movie_id_entity)

    return views.responses.movie.CreateMovieResponse.new(movie_id)


@router.delete("/{id}", dependencies=[dependencies.auth.EnsureCurrentSuperUserIdDependency])
async def delete_movie(
    delete_movie_usecase: dependencies.usecases.DeleteMovieUsecaseDependency,
    movie_id: dependencies.path.MovieIdFromPathDependency,
) -> views.responses.movie.DeleteMovieResponse:
    deleted_movie_id_entity = await delete_movie_usecase.execute(movie_id=movie_id.to_entity())

    deleted_movie_id = views.movie.MovieId.from_entity(deleted_movie_id_entity)

    return views.responses.movie.DeleteMovieResponse.new(deleted_movie_id)


@router.get("/{id}/reviews", dependencies=[dependencies.auth.EnsureCurrentUserIdDependency])
async def get_all_movie_reviews(
    get_all_movie_reviews_usecase: dependencies.usecases.GetAllMovieReviewsUsecaseDependency,
    movie_id: dependencies.path.MovieIdFromPathDependency,
) -> views.responses.movie.GetAllMovieReviewsResponse:
    review_for_movie_entities = await get_all_movie_reviews_usecase.execute(movie_id.to_entity())

    reviews_for_movie = [
        views.reviews.ReviewForMovie.from_entity(review_for_movie_entity)
        for review_for_movie_entity in review_for_movie_entities
    ]
    return views.responses.movie.GetAllMovieReviewsResponse.new(reviews_for_movie=reviews_for_movie)
