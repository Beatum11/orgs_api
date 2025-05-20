from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from ..config import settings
from ..organizations.models import Base

engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=True
)

async_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def init_db():
    async with engine.begin() as conn:
        conn.run_sync(Base.metadata.create_all)

async def get_session():
    async with async_session() as session:
        yield session