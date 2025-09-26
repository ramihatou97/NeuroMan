from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from .settings import settings

# Async engine using DATABASE_URL from config
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
    future=True,
)

# Session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
)


async def get_db():
    """
    FastAPI dependency — yields an AsyncSession and
    ensures it is closed after the request.
    """
    async with AsyncSessionLocal() as session:
        yield session