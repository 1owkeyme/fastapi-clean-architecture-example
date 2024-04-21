from domain import entities, usecases
from domain.entities.movie import MovieId, MovieInfo
from domain.entities.review import ReviewId, ReviewInfo


class SQLAlchemy(
    usecases.auth.interfaces.UserRepository,
    usecases.movie.interfaces.MovieRepository,
    usecases.review.interfaces.ReviewRepository,
):
    async def create_user(
        self,
        credentials: entities.user.Credentials,
    ) -> None:
        print(f"Created user new user: {credentials}")

    async def create_movie(self, info: MovieInfo) -> None:
        print(f"Created new movie: {info}")

    async def create_review(self, info: ReviewInfo) -> None:
        print(f"Created new review: {info}")

    async def delete_review(self, id_: ReviewId) -> None:
        print(f"Deleted review: {id_}")

    async def delete_movie(self, id_: MovieId) -> None:
        print(f"Deleted movie: {id_}")
