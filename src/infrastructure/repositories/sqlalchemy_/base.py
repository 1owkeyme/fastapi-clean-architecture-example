import typing as t
from asyncio import current_task
from contextlib import _AsyncGeneratorContextManager, asynccontextmanager

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)


class AlchemyBaseRepository:
    def _get_scoped_session_factory(
        self, url: str, echo: bool = False
    ) -> t.Callable[[], _AsyncGeneratorContextManager[async_scoped_session[AsyncSession]]]:
        engine = create_async_engine(url=url, echo=echo)
        self._session_factory = async_sessionmaker(
            bind=engine,
            autoflush=False,
            expire_on_commit=False,
        )

        @asynccontextmanager
        async def __get_scoped_session() -> t.AsyncIterator[async_scoped_session[AsyncSession]]:
            scoped_session = async_scoped_session(self._session_factory, scopefunc=current_task)
            try:
                yield scoped_session
            except Exception as exc:
                await scoped_session.rollback()
                raise exc
            finally:
                await scoped_session.close()

        return __get_scoped_session
