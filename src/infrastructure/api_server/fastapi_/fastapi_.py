from fastapi import FastAPI

from .. import interfaces
from .routers import users


class FastAPIServer(interfaces.APIServer):
    def _get_asgi_app(self) -> FastAPI:
        app = FastAPI()

        app.include_router(users.router, prefix="/users", tags=["users"])

        return app
