from UniSystem.infra.postgres.connection import async_session
from UniSystem.infra.postgres.tables import *
from sqlalchemy.future import select


async def find_academic(academic_email):
    async with async_session() as session:
        academic_data = await session.execute(select(AcademicInstitutionalData).
                                              where(AcademicInstitutionalData.institutional_email == academic_email))

        academic_data_row = academic_data.scalars().first()

        data = {
            'registration': academic_data_row.registration,
            'name': academic_data_row.name,
            'institutional_email': academic_data_row.institutional_email,
            'academic_type_id': academic_data_row.academic_type_id,
            'password': academic_data_row.password
        }

        return data


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
            'registration': dean_institutional_row.registration,
            'name': dean_institutional_row.name,
            'institutional_email': dean_institutional_row.institutional_email,
            'registration_date': dean_info_row.registration_date,
            'rectory_entry_date': dean_info_row.rectory_entry_date,
            'rectory_exit_date': dean_info_row.rectory_exit_date,
            'salary': dean_info_row.salary,
            'academic_training_place': dean_info_row.academic_training_place
        }

        return data


async def find_principal(principal_registration):
    async with async_session() as session:
        principal_institutional_data = await session.execute(select(AcademicInstitutionalData).where
            (AcademicInstitutionalData.registration == principal_registration))

        principal_info = await session.execute(select(Deans).where(Deans.registration == principal_registration))

        principal_info_row = principal_info.scalars().first()
        principal_institutional_row = principal_institutional_data.scalars().first()

        data = {
            'registration': principal_institutional_row.registration,
            'name': principal_institutional_row.name,
            'institutional_email': principal_institutional_row.institutional_email,
            'registration_date': principal_info_row.registration_date,
            'entry_board_date': principal_info_row.entry_board_date,
            'exit_board_date': principal_info_row.exit_board_date,
            'salary': principal_info_row.salary,
            'vice_principal': principal_info_row.vice_principal
        }

        return data


async def find_subject(subject_id):
    async with async_session() as session:
        subject_data = session.execute(select(Subjects).where(Subjects.id == subject_id))

        subject_data_row = subject_data.scalars().first()

        data = {
            'id': subject_data_row.id,
            'professor_registration': subject_data_row.professor_registration,
            'course': subject_data_row.course,
            'subject_name': subject_data_row.subject_name,
            'workload': subject_data_row.workload
        }

        return data


async def find_student_subject_notes(student_registration):
    async with async_session() as session:
        subject_note_data = await session.execute(select(SubjectsNotes).where
                                            (SubjectsNotes.student_registration == student_registration))

        subject_note_data_rows = subject_note_data.scalars()

        data = {}

        i = 1
        for obj in subject_note_data_rows:
            row = {
                'subjects_id': obj.subject_id,
                'student_registration': obj.student_registration,
                'professor_registration': obj.professor_registration,
                'subject_start_date': obj.subject_start_date,
                'note': obj.note,
                'note_date': obj.note_date,
                'approved': obj.approved
            }
            data[i] = row

            i = i+1

        return data


async def find_subject_notes(subject_id):
    async with async_session() as session:
        subject_notes_data = await session.execute(select(SubjectsNotes).where(SubjectsNotes.subjects_id == subject_id))

        subject_notes_data_rows = subject_notes_data.scalars()

        data = {}

        i = 1
        for obj in subject_notes_data_rows:
            row = {
                'subjects_id': obj.subject_id,
                'student_registration': obj.student_registration,
                'professor_registration': obj.professor_registration,
                'subject_start_date': obj.subject_start_date,
                'note': obj.note,
                'note_date': obj.note_date,
                'approved': obj.approved
            }
            data[i] = row

            i = i + 1

        return data


async def find_subject_notes_by_date(subject_notes_date):
    async with async_session() as session:
        subject_notes_date_data = session.execute(select(SubjectsNotes).
                                                  where(SubjectsNotes.note_date == subject_notes_date))

        subject_notes_date_data_rows = subject_notes_date_data.scalars()

        data = {}

        i = 1
        for obj in subject_notes_date_data_rows:
            row = {
                'subjects_id': obj.subject_id,
                'student_registration': obj.student_registration,
                'professor_registration': obj.professor_registration,
                'subject_start_date': obj.subject_start_date,
                'note': obj.note,
                'note_date': obj.note_date,
                'approved': obj.approved
            }
            data[i] = row

            i = i + 1

        return data


async def sum_subject_notes(subject_id, subject_note_date):
    async with async_session() as session:
        subject_note_data = session.execute(select(SubjectsNotes).where(
            SubjectsNotes.subjects_id == subject_id, SubjectsNotes.note_date == subject_note_date))

        subject_note_data_rows = subject_note_data.scalars()

        subject_notes_sum = session.func.sum(subject_note_data_rows.note)

        return subject_notes_sum


async def max_subject_notes(subject_id):
    async with async_session() as session:
        subject_note_data = session.execute(select(SubjectsNotes).where(SubjectsNotes.subjects_id == subject_id))

        subject_note_data_rows = subject_note_data.scalars()

        subject_note_max = session.func.max(subject_note_data_rows.note)

        return subject_note_max


async def min_subject_notes(subject_id):
    async with async_session() as session:
        subject_note_data = session.execute(select(SubjectsNotes).where(SubjectsNotes.subjects_id == subject_id))

        subject_note_data_rows = subject_note_data.scalars()

        subject_note_min = session.func.min(subject_note_data_rows.note)

        return subject_note_min


async def avg_subject_notes(subject_id):
    async with async_session() as session:
        subject_note_data = session.execute(select(SubjectsNotes).where(SubjectsNotes.subjects_id == subject_id))

        subject_note_data_rows = subject_note_data.scalars()

        subject_note_avg = session.func.avg(subject_note_data_rows.note)

        return subject_note_avg


async def count_subject_notes(subject_id):
    async with async_session() as session:
        subject_notes_data = session.execute(select(SubjectsNotes).where(SubjectsNotes.subjects_id == subject_id))

        subject_notes_data_rows = subject_notes_data.scalars()

        subject_note_count = session.func.count(subject_notes_data_rows)

        return subject_note_count
