from abc import ABC, abstractmethod

from domain import entities


class MovieRepository(ABC):
    @abstractmethod
    async def get_movie_by_id(self, id_entity: entities.Id) -> entities.movie.Movie:
        pass

    @abstractmethod
    async def get_all_movies(self) -> list[entities.movie.Movie]:
        pass

    @abstractmethod
    async def create_movie(self, info_entity: entities.movie.MovieInfo) -> entities.Id:
        pass

    @abstractmethod
    async def delete_movie_by_id(self, id_entity: entities.Id) -> entities.Id:
        pass

    @abstractmethod
    async def get_all_movie_reviews_by_id(self, id_entity: entities.Id) -> list[entities.review.ReviewForMovie]:
        pass
