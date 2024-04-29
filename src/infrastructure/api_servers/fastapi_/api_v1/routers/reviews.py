from fastapi import APIRouter

from domain import usecases

from . import dependencies, responses, schemas


router = APIRouter()


@router.get("/{review_id}", dependencies=[dependencies.auth.EnsureCurrentSuperUserDependency])
async def get_review_by_id(
    get_review_by_id_usecase: dependencies.usecases.review.GetReviewByIdUsecaseDependency,
    review_id: dependencies.path.ReviewIdFromPathDependency,
) -> responses.review.GetReviewByIdResponse | responses.review.ReviewNotFoundErrorResponse:
    try:
        review_entity = await get_review_by_id_usecase.execute(review_id.to_id_entity())
    except usecases.review.errors.ReviewNotFoundError:
        return responses.review.ReviewNotFoundErrorResponse.new()

    review = schemas.review.Review.from_entity(review_entity)
    return responses.review.GetReviewByIdResponse.new(review=review)


@router.post("/{movie_id}")
async def create_review_by_movie_id(
    create_review_schema: schemas.review.CreateReview,
    current_user: dependencies.auth.CurrentUserDependency,
    movie_id: dependencies.path.MovieIdFromPathDependency,
    create_review_by_movie_id_usecase: dependencies.usecases.review.CreateReviewByMovieIdUsecaseDependency,
    get_movie_by_id_usecase: dependencies.usecases.movie.GetMovieByIdUsecaseDependency,
) -> (
    responses.review.CreateReviewResponse
    | responses.movie.MovieNotFoundErrorResponse
    | responses.review.ReviewAlreadyExistsErrorResponse
):
    user_id_entity = current_user.to_id_entity()
    movie_id_entity = movie_id.to_id_entity()
    review_info_entity = create_review_schema.to_entity()
    try:
        review_id_entity = await create_review_by_movie_id_usecase.execute(
            user_id=user_id_entity,
            movie_id=movie_id_entity,
            review_info=review_info_entity,
            get_movie_by_id_usecase=get_movie_by_id_usecase,
        )
    except usecases.movie.errors.MovieNotFoundError:
        return responses.movie.MovieNotFoundErrorResponse.new()
    except usecases.review.errors.ReviewAlreadyExistsError:
        return responses.review.ReviewAlreadyExistsErrorResponse.new()

    review_id_schema = schemas.review.ReviewId.from_id_entity(review_id_entity)
    return responses.review.CreateReviewResponse.new(id_=review_id_schema.review_id)


@router.delete("/{review_id}", dependencies=[dependencies.auth.EnsureCurrentSuperUserDependency])
async def delete_review_by_id(
    delete_review_by_id_usecase: dependencies.usecases.review.DeleteReviewByIdUsecaseDependency,
    review_id: dependencies.path.ReviewIdFromPathDependency,
) -> responses.review.DeleteReviewByIdResponse | responses.review.ReviewNotFoundErrorResponse:
    try:
        deleted_review_id_entity = await delete_review_by_id_usecase.execute(review_id.to_id_entity())
    except usecases.review.errors.ReviewNotFoundError:
        return responses.review.ReviewNotFoundErrorResponse.new()
    deleted_review_id_schema = schemas.review.ReviewId.from_id_entity(deleted_review_id_entity)
    return responses.review.DeleteReviewByIdResponse.new(id_=deleted_review_id_schema.review_id)
