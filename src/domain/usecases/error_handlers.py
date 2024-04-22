import typing as t


T = t.TypeVar("T")
P = t.ParamSpec("P")


def handle_unhandled(func: t.Callable[P, T]) -> t.Callable[P, t.Awaitable[T]]:
    async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            raise

    return wrapper
