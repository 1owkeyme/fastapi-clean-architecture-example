from abc import ABC, abstractmethod

import uvicorn
from starlette.applications import Starlette


class APIServerBase(ABC):
    def run(self, port: int) -> None:
        config = uvicorn.Config(self._get_asgi_app(), host="0.0.0.0", port=port)

        uvicorn.Server(config).run()

    @abstractmethod
    def _get_asgi_app(self) -> Starlette:
        pass
