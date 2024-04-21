from abc import ABC, abstractmethod

from domain import entities


class MovieRepository(ABC):
    @abstractmethod
    async def create_movie(self, info: entities.movie.MovieInfo) -> None:
        pass

    @abstractmethod
    async def delete_movie(self, id_: entities.movie.MovieId) -> None:
        pass
