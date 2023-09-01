from UniSystem.domain.schemas import *
from UniSystem.infra.postgres.connection import async_session
from UniSystem.infra.postgres.tables import *
from UniSystem.application.security import get_hash_password


async def professor_register_query(professor: Professor):
    hashed_password = get_hash_password(professor.password)
    professor.academic_type_id = 2
    professor.professional_status = 'professor'
    async with async_session() as session:
        session.add(Professors(registration=professor.registration, name=professor.name,
                               registration_date=professor.registration_date,
                               institutional_email=professor.institutional_email, password=hashed_password,
                               academic_type_id=professor.academic_type_id,
                               academic_formation=professor.academic_formation,
                               academic_status=professor.academic_status,
                               professional_status=professor.professional_status,
                               salary=professor.salary, academic_training_place=professor.academic_training_place))
        await session.commit()


async def student_register_query(student: Student):
    hashed_password = get_hash_password(student.password)
    student.academic_type_id = 1
    student.academic_period = 1
    student.coefficient = 0
    async with async_session() as session:
        session.add(Students(registration=student.registration, name=student.name,
                             registration_date=student.registration_date,
                             institutional_email=student.institutional_email,
                             password=hashed_password, academic_type_id=student.academic_type_id,
                             coefficient=student.coefficient, academic_period=student.academic_period,
                             course=student.course))
        await session.commit()


async def subject_register_query(subject: Subject):
    async with async_session() as session:
        session.add(Subjects(id=subject.id, professor_registration=subject.professor_registration,
                             course=subject.course, subject_name=subject.subject_name,
                             workload=subject.workload))
        await session.commit()


async def dean_register_query(dean: Dean):
    hashed_password = get_hash_password(dean.password)
    dean.academic_type_id = 3
    async with async_session() as session:
        session.add(Deans(registration=dean.registration, name=dean.name,
                          registration_date=dean.registration_date,
                          institutional_email=dean.institutional_email,
                          password=hashed_password, academic_type_id=dean.academic_type_id,
                          rectory_entry_date=dean.rectory_entry_date,
                          rectory_exit_date=dean.rectory_exit_date,
                          academic_training_place=dean.academic_training_place))
        session.commit()


async def principal_register_query(principal: Principal):
    hashed_password = get_hash_password(principal.password)
    principal.academic_type_id = 2
    principal.professional_status = 'Principal'
    async with async_session() as session:
        session.add(Principals(registration=principal.registration, name=principal.name,
                               registration_date=principal.registration_date,
                               institutional_email=principal.institutional_email,
                               password=hashed_password, academic_type_id=principal.academic_type_id,
                               academic_formation=principal.academic_formation,
                               academic_status=principal.academic_status,
                               professional_status=principal.professional_status,
                               salary=principal.salary, academic_training_place=principal.academic_training_place,
                               entry_board_date=principal.entry_board_date, exit_board_date=principal.exit_board_date,
                               vice_principal=principal.vice_principal))
        session.commit()


async def subject_notes_register_query(subnote: SubjectNote):
    async with async_session() as session:
        session.add(SubjectsNotes(subjects_id=subnote.subject_id, student_registration=subnote.student_registration,
                                  professor_registration=subnote.professor_registration, note=subnote.note,
                                  note_date=subnote.note_date))
