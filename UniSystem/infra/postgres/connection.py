from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool


url = 'postgresql+asyncpg://postgres:asunder32@localhost:5434/UniSystem_1'
engine = create_async_engine(url, poolclass=NullPool)
async_session = sessionmaker(engine, class_=AsyncSession)