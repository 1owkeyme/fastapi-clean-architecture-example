import typing as t

from .interfaces import errors as err


T = t.TypeVar("T")
P = t.ParamSpec("P")


def handle_usecases_errors(func: t.Callable[P, t.Awaitable[T]]) -> t.Callable[P, t.Awaitable[T]]:
    async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        try:
            return await func(*args, **kwargs)
        except err.UsecaseError:
            raise
        except err.UsecaseCriticalError:
            raise
        except Exception as exc:
            raise err.UsecaseCriticalError from exc

    return wrapper
