from fastapi import APIRouter

from . import dependencies, schemas, views


router = APIRouter()


@router.get("/{id}", dependencies=[dependencies.auth.EnsureCurrentSuperUserIdDependency])
async def get_review_by_id(
    get_review_by_id_usecase: dependencies.usecases.GetReviewByIdUsecaseDependency,
    review_id: dependencies.path.ReviewIdFromPathDependency,
) -> views.responses.GetReviewByIdResponse:
    review_entity = await get_review_by_id_usecase.execute(review_id.to_entity())

    review = views.reviews.Review.from_entity(review_entity)
    return views.responses.GetReviewByIdResponse.new(review=review)


@router.post("/{id}")
async def create_review(
    create_review_usecase: dependencies.usecases.CreateReviewUsecaseDependency,
    create_review_schema: schemas.reviews.CreateReviewSchema,
    current_user_id: dependencies.auth.CurrentUserIdDependency,
    movie_id: dependencies.path.MovieIdFromPathDependency,
) -> views.responses.CreateReviewResponse:
    user_id_entity = current_user_id.to_entity()
    movie_id_entity = movie_id.to_entity()
    review_contents_entity = create_review_schema.to_review_contents_entity()

    review_id_entity = await create_review_usecase.execute(
        user_id=user_id_entity,
        movie_id=movie_id_entity,
        review_contents=review_contents_entity,
    )

    review_id = views.reviews.ReviewId.from_review_id_entity(review_id_entity)

    return views.responses.CreateReviewResponse.new(review_id=review_id)


@router.delete("/{id}", dependencies=[dependencies.auth.EnsureCurrentSuperUserIdDependency])
async def delete_review(
    delete_review_usecase: dependencies.usecases.DeleteReviewUsecaseDependency,
    review_id: dependencies.path.ReviewIdFromPathDependency,
) -> views.responses.DeleteReviewResponse:
    deleted_review_id_entity = await delete_review_usecase.execute(review_id.to_entity())

    deleted_review_id = views.reviews.ReviewId.from_review_id_entity(deleted_review_id_entity)
    return views.responses.DeleteReviewResponse.new(id_=deleted_review_id)
