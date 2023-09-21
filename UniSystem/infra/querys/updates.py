from UniSystem.domain.schemas import Dean, Principal, Professor, Student
from UniSystem.infra.postgres.tables import Deans, Principals, Professors, Students, Subjects, SubjectsNotes
from UniSystem.application.security import get_hash_password
from sqlalchemy.future import select
from UniSystem.infra.postgres.connection import async_session


async def update_principal_account(principal_registration, field: str, value):
    field = field.lower()
    if field == 'name':
        async with async_session() as session:
            principal_data = session.execute(select(Principal).where(Principal.registration == principal_registration))
            principal_data_row = principal_data.scalars().first()

            principal_data_row.name = value
            session.commit()
    if field == 'institutional_email':
        async with async_session() as session:
            principal_data = session.execute(select(Principal).where(Principal.registration == principal_registration))
            principal_data_row = principal_data.scalars().first()

            principal_data_row.institutional_email = value
            session.commit()
    if field == 'password':
        async with async_session() as session:
            principal_data = session.execute(select(Principal).where(Principal.registration == principal_registration))
            principal_data_row = principal_data.scalars().first()

            password = get_hash_password(value)
            principal_data_row.password = password
            session.commit()
