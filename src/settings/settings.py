import functools
import typing as t

from .app import AppSettings
from .base import AppEnv, BaseAppSettings
from .dev import DevAppSettings
from .prod import ProdAppSettings


app_environment_to_settings_cls: dict[AppEnv, t.Type[AppSettings]] = {
    AppEnv.DEV: DevAppSettings,
    AppEnv.PROD: ProdAppSettings,
}


@functools.cache
def get_app_settings() -> AppSettings:
    app_env = BaseAppSettings().APP_ENV
    app_settings_cls = app_environment_to_settings_cls[app_env]
    return app_settings_cls()  # type: ignore
