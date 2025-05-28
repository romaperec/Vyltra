from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.config import database_config

engine = create_async_engine(
    url=database_config.DATABASE_URL, echo=database_config.DATABASE_ECHO
)
sessionmaker = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def get_session():
    async with sessionmaker() as session:
        yield session
