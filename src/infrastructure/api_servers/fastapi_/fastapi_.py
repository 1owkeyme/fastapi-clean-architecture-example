from fastapi import FastAPI

from ..base import APIServerBase
from .routers import users


class FastAPIServer(APIServerBase):
    def _get_asgi_app(self) -> FastAPI:
        app = FastAPI()

        app.include_router(users.router, prefix="/users", tags=["users"])

        return app
