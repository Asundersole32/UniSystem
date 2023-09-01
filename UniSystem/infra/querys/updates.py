from UniSystem.domain.schemas import Dean, Principal, Professor, Student
from UniSystem.infra.postgres.tables import Deans, Principals, Professors, Students, Subjects, SubjectsNotes
from UniSystem.infra.postgres.connection import async_session


async def dean_update_query(field: str, value):
    async with async_session() as session:
        if field == 'name':
            dean = session.query(Deans)