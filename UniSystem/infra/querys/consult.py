from UniSystem.infra.postgres.connection import async_session
from UniSystem.infra.postgres.tables import *
from sqlalchemy.future import select


async def find_student(student_registration):
    async with async_session() as session:
        student_institutional_data = await session.execute(select(AcademicInstitutionalData).where
                                                     (AcademicInstitutionalData.registration == student_registration))
        student_info = await session.execute(select(Students).where(Students.registration == student_registration))

        student_data_row = student_info.scalars().first()
        student_institutional_row = student_institutional_data.scalars().first()

        data = {
            'registration': student_institutional_row.registration,
            'name': student_institutional_row.name,
            'institutional_email': student_institutional_row.institutional_email,
            'registration_date': student_data_row.registration_date,
            'coefficient': student_data_row.coefficient,
            'academic_period': student_data_row.academic_period,
            'course': student_data_row.course
        }

        return data


async def find_professor(professor_registration):
    async with async_session.begin() as session:
        professor_institutional_data = await session.execute(
            select(AcademicInstitutionalData).
            where(AcademicInstitutionalData.registration == professor_registration))
        professor_info_data = await session.execute(select(Professors).
                                                    where(Professors.registration == professor_registration))

        professor_data_row = professor_info_data.scalars().first()
        professor_institutional_row = professor_institutional_data.scalars().first()

        data = {
            'registration': professor_institutional_row.registration,
            'name': professor_institutional_row.name,
            'institutional_email': professor_institutional_row.institutional_email,
            'registration_date': professor_data_row.registration_date,
            'academic_formation': professor_data_row.academic_formation,
            'academic_status': professor_data_row.academic_status,
            'salary': professor_data_row.salary,
            'academic_training_place': professor_data_row.academic_training_place
        }

        return data



async def find_dean(dean_registration):
    async with async_session() as session:
        dean_institutional_data = await session.execute(select(AcademicInstitutionalData).where
            (AcademicInstitutionalData.registration == dean_registration))
        dean_info = await session.execute(select(Deans.registration).where(Deans.registration == dean_registration))

        dean_info_row = dean_info.scalars().first()
        dean_institutional_row = dean_institutional_data.scalars().first()

        data = {

        }

        return data


async def find_principal(principal_registration):
    async with async_session() as session:
        principal_institutional_data = session.query(AcademicInstitutionalData).filter\
            (AcademicInstitutionalData.registration == principal_registration).first()
        principal_info = session.query(Deans).filter(Deans.registration == principal_registration).first()

        return [principal_institutional_data, principal_info]


async def find_subject(subject_id):
    async with async_session() as session:
        subject_data = session.query(Subjects).filter(Subjects.id == subject_id).first()

        return subject_data


async def find_student_subject_notes(student_registration):
    async with async_session() as session:
        subject_note_data = session.query(SubjectsNotes).filter\
            (SubjectsNotes.student_registration == student_registration).all()

        return subject_note_data


async def find_subject_notes(subject_id):
    async with async_session() as session:
        subject_notes_data = session.query(SubjectsNotes).filter(SubjectsNotes.subjects_id == subject_id).all()

        return subject_notes_data


async def find_subject_notes_by_date(subject_notes_date):
    async with async_session() as session:
        subject_notes_date_data = session.query(SubjectsNotes).filter(SubjectsNotes.note_date == subject_notes_date).\
            all()

        return subject_notes_date_data


async def sum_subject_notes(subject_id, subject_note_date):
    async with async_session() as session:
        subject_note_data = session.query(SubjectsNotes).filter(
            SubjectsNotes.subjects_id == subject_id, SubjectsNotes.note_date == subject_note_date).all()

        subject_notes_sum = session.func.sum(subject_note_data.note)

        return subject_notes_sum


async def max_subject_notes(subject_id):
    async with async_session() as session:
        subject_note_data = session.query(SubjectsNotes).filter(SubjectsNotes.subjects_id == subject_id).all()

        subject_note_max = session.func.max(subject_note_data.note)

        return subject_note_max


async def min_subject_notes(subject_id):
    async with async_session() as session:
        subject_note_data = session.query(SubjectsNotes).filter(SubjectsNotes.subjects_id == subject_id).all()

        subject_note_min = session.func.min(subject_note_data.note)

        return subject_note_min


async def avg_subject_notes(subject_id):
    async with async_session() as session:
        subject_note_data = session.query(SubjectsNotes).filter(SubjectsNotes.subjects_id == subject_id).all()

        subject_note_avg = session.func.avg(subject_note_data.note)

        return subject_note_avg


async def count_subject_notes(subject_id):
    async with async_session() as session:
        subject_notes_data = session.query(SubjectsNotes).filter(SubjectsNotes.subjects_id == subject_id).all()

        subject_note_count = session.func.count(subject_notes_data)

        return subject_note_count
