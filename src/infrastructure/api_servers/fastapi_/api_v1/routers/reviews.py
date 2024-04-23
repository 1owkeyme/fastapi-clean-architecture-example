from fastapi import APIRouter

from . import dependencies, schemas, views


router = APIRouter()


@router.get("/{review_id}", dependencies=[dependencies.auth.EnsureCurrentSuperUserIdDependency])
async def get_review_by_id(
    get_review_by_id_usecase: dependencies.usecases.GetReviewByIdUsecaseDependency,
    review_id: dependencies.path.ReviewIdFromPathDependency,
) -> views.responses.review.GetReviewByIdResponse:
    review_entity = await get_review_by_id_usecase.execute(review_id.to_entity())

    review = views.reviews.Review.from_entity(review_entity)
    return views.responses.review.GetReviewByIdResponse.new(review=review)


@router.post("/{movie_id}")
async def create_review_by_movie_id(
    create_review_usecase: dependencies.usecases.CreateReviewUsecaseDependency,
    create_review_schema: schemas.reviews.CreateReviewSchema,
    current_user_id: dependencies.auth.CurrentUserIdDependency,
    movie_id: dependencies.path.MovieIdFromPathDependency,
) -> views.responses.review.CreateReviewResponse:
    user_id_entity = current_user_id.to_entity()
    movie_id_entity = movie_id.to_entity()
    review_contents_entity = create_review_schema.to_review_contents_entity()

    review_id_entity = await create_review_usecase.execute(
        user_id=user_id_entity,
        movie_id=movie_id_entity,
        review_contents=review_contents_entity,
    )

    review_id = views.reviews.ReviewId.from_review_id_entity(review_id_entity)

    return views.responses.review.CreateReviewResponse.new(review_id=review_id)


@router.delete("/{review_id}", dependencies=[dependencies.auth.EnsureCurrentSuperUserIdDependency])
async def delete_review_by_id(
    delete_review_usecase: dependencies.usecases.DeleteReviewUsecaseDependency,
    review_id: dependencies.path.ReviewIdFromPathDependency,
) -> views.responses.review.DeleteReviewResponse:
    deleted_review_id_entity = await delete_review_usecase.execute(review_id.to_entity())

    deleted_review_id = views.reviews.ReviewId.from_review_id_entity(deleted_review_id_entity)
    return views.responses.review.DeleteReviewResponse.new(id_=deleted_review_id)
