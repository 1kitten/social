from asyncio import current_task
from collections.abc import AsyncGenerator
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import async_scoped_session, create_async_engine, async_sessionmaker
from config import settings


class Base(DeclarativeBase):
    pass


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )
    
    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task
        )
        return session

    async def session_dependency(self) -> AsyncGenerator:
        session = self.get_scoped_session()

        async with session() as sess:
            yield sess
            await session.remove()


db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.db_echo
)
