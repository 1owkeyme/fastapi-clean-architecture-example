from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware

from domain import usecases

from ..base import APIServerBase
from . import api_v1


def _generate_unique_id_function(route: APIRoute) -> str:
    return f"{route.tags[0]}:{route.name}"


class FastAPIServer(APIServerBase):
    def __init__(
        self,
        auth_usecases_builder: usecases.auth.AuthUsecasesBuilder,
        app_title: str,
        api_v1_prefix: str,
        openapi_url: str,
        cors_origins: list[str],
    ) -> None:
        self.__auth_usecases_builder = auth_usecases_builder

        self.__app_title = app_title
        self.__openapi_url = openapi_url
        self.__api_v1_prefix = api_v1_prefix
        self.__cors_origins = cors_origins

    def _get_asgi_app(self) -> FastAPI:
        app = FastAPI(
            title=self.__app_title,
            openapi_url=self.__openapi_url,
            generate_unique_id_function=_generate_unique_id_function,
        )

        if len(self.__cors_origins):
            app.add_middleware(
                CORSMiddleware,
                allow_origins=self.__cors_origins,
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )

        api_v1_router = api_v1.get_api_router(
            auth_usecases_builder=self.__auth_usecases_builder
        )

        app.include_router(api_v1_router)

        return app
