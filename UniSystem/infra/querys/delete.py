from UniSystem.infra.postgres.connection import async_session
from UniSystem.infra.postgres.tables import *
from sqlalchemy.future import select


async def del_student(student_registration):
    async with async_session() as session:
        student_data = await session.execute(select(Students).where(Students.registration == student_registration))

        student_data_row = student_data.scalars().first()

        session.delete(student_data_row)
        session.commit()


async def del_professor(professor_registration):
    async with async_session() as session:
        professor_data = await session.execute(select(Professors).where
                                               (Professors.registration == professor_registration))

        professor_data_row = professor_data.scalars().first()

        session.delete(professor_data_row)
        session.commit()


async def del_subject(subject_id):
    async with async_session() as session:
        subject_data = await session.execute(select(Subjects).where(Subjects.id == subject_id))

        subject_data_row = subject_data.scalars().first()

        session.delete(subject_data_row)
        session.commit()


async def del_principal(principal_registration):
    async with async_session() as session:
        principal_data = await session.execute(select(Professors).where
                                               (Professors.registration == principal_registration))

        principal_data_row = principal_data.scalars().first()

        session.delete(principal_data_row)
        session.commit()


async def del_subject_student_notes(student_registration):
    async with async_session() as session:
        subject_notes_data = await session.execute(select(SubjectsNotes).where
                                                   (SubjectsNotes.student_registration == student_registration))

        subject_notes_data_rows = subject_notes_data.scalars()

        session.delete(subject_notes_data_rows)
        session.commit()


async def del_subject_notes(subject_id):
    async with async_session() as session:
        subject_notes_data = await session.execute(select(SubjectsNotes).where(SubjectsNotes.subjects_id == subject_id))

        subject_notes_data_rows = subject_notes_data.scalars()

        session.delete(subject_notes_data_rows)
        session.commit()
