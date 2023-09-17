from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from UniSystem.util.env_conection import env_connection_values


engine = create_async_engine(env_connection_values('URL'), poolclass=NullPool)
async_session = sessionmaker(engine, class_=AsyncSession)
