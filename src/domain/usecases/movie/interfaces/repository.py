from abc import ABC, abstractmethod

from domain import entities


class MovieRepository(ABC):
    @abstractmethod
    async def get_all_movies(self) -> list[entities.movie.Movie]:
        pass

    @abstractmethod
    async def create_movie(self, info_entity: entities.movie.MovieInfo) -> None:
        pass

    @abstractmethod
    async def delete_movie(self, id_entity: entities.movie.MovieId) -> None:
        pass
