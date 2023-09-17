from UniSystem.infra.postgres.connection import engine, async_session
from UniSystem.infra.postgres.tables import Base, new_academic_type1, new_academic_type2, new_academic_type3, new_academic_type4


async def create_database():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


async def academic_type_insert():
    async with async_session() as session:
        session.add(new_academic_type1)
        session.add(new_academic_type2)
        session.add(new_academic_type3)
        session.add(new_academic_type4)
        await session.commit()
