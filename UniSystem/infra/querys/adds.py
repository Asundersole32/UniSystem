from UniSystem.domain.schemas import *
from UniSystem.infra.postgres.connection import async_session
from UniSystem.infra.postgres.tables import *
from UniSystem.application.security import get_hash_password

from sqlalchemy.future import select


async def admin_register_query(admin: Academic):
    hashed_password = get_hash_password(admin.password)
    async with async_session() as session:
        session.add(AcademicInstitutionalData(registration=admin.registration, academic_type_id=5,
                                              name=admin.name, institutional_email=admin.institutional_email,
                                              password=hashed_password))

        await session.commit()


async def professor_register_query(professor: Professor):
    hashed_password = get_hash_password(professor.password)
    async with async_session() as session:
        session.add(Professors(registration=professor.registration,
                               registration_date=professor.registration_date,
                               academic_formation=professor.academic_formation,
                               academic_status=professor.academic_status,
                               salary=professor.salary, academic_training_place=professor.academic_training_place))

        session.add(AcademicInstitutionalData(registration=professor.registration, academic_type_id=2,
                                              name=professor.name,
                                              institutional_email=professor.institutional_email,
                                              password=hashed_password))

        await session.commit()


async def student_register_query(student: Student):
    hashed_password = get_hash_password(student.password)
    academic_period = 1
    coefficient = 0
    async with async_session() as session:
        session.add(Students(registration=student.registration,
                             registration_date=student.registration_date,
                             coefficient=coefficient, academic_period=academic_period,
                             course=student.course))

        session.add(AcademicInstitutionalData(registration=student.registration, academic_type_id=1,
                                              name=student.name,
                                              institutional_email=student.institutional_email,
                                              password=hashed_password))
        await session.commit()


async def subject_register_query(subject: Subject):
    async with async_session() as session:
        session.add(Subjects(id=subject.id, professor_registration=subject.professor_registration,
                             course=subject.course, subject_name=subject.subject_name,
                             workload=subject.workload))
        await session.commit()


async def dean_register_query(dean: Dean):
    hashed_password = get_hash_password(dean.password)
    async with async_session() as session:
        session.add(Deans(registration=dean.registration,
                          registration_date=dean.registration_date,
                          rectory_entry_date=dean.rectory_entry_date,
                          rectory_exit_date=dean.rectory_exit_date,
                          academic_training_place=dean.academic_training_place))

        session.add(AcademicInstitutionalData(registration=dean.registration, academic_type_id=4,
                                              name=dean.name,
                                              institutional_email=dean.institutional_email,
                                              password=hashed_password))

        await session.commit()


async def principal_register_query(principal: Principal):
    async with async_session() as session:
        session.add(Principals(registration=principal.registration,
                               entry_board_date=principal.entry_board_date, exit_board_date=principal.exit_board_date,
                               salary=principal.salary,
                               vice_principal=principal.vice_principal))

        academic_data = await session.execute(select(AcademicInstitutionalData).
                                        where(AcademicInstitutionalData.registration == principal.registration))

        academic_data_row = academic_data.scalars().first()
        academic_data_row.academic_type_id = 3

        await session.commit()


async def subject_notes_register_query(subject_note: SubjectNote):
    async with async_session() as session:
        session.add(SubjectsNotes(subjects_id=subject_note.subject_id, student_registration=subject_note.student_registration,
                                  professor_registration=subject_note.professor_registration, note=subject_note.note,
                                  note_date=subject_note.note_date))

        await session.commit()
