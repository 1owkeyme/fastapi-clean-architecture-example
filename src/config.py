import functools
import typing as t

from settings import (
    AppEnv,
    AppSettings,
    BaseAppSettings,
    DevAppSettings,
    ProdAppSettings,
    TestAppSettings,
)

app_environments: dict[AppEnv, t.Type[AppSettings]] = {
    AppEnv.DEV: DevAppSettings,
    AppEnv.PROD: ProdAppSettings,
    AppEnv.TEST: TestAppSettings,
}


@functools.cache
def get_app_config() -> AppSettings:
    app_env = BaseAppSettings().app_env
    return app_environments[app_env]()
