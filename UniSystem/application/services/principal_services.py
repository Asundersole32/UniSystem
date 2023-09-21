from UniSystem.domain.schemas import *
from UniSystem.infra.querys.adds import *
from UniSystem.infra.querys.consult import *
from UniSystem.application.exceptions.http_exceptions import *
from UniSystem.infra.querys.delete import *
from UniSystem.infra.querys.updates import *


async def update_account_service(principal_registration: str, field: str, value):
    try:
        await update_principal_account(principal_registration, field, value)
    except Exception as e:
        bad_request(e)


async def cad_professor_service(professor: Professor):
    try:
        await professor_register_query(professor)
    except Exception as e:
        bad_request(e)


async def cad_student_service(student: Student):
    try:
        await student_register_query(student)
    except Exception as e:
        bad_request(e)


async def cad_subject_service(subject: Subject):
    try:
        await subject_register_query(subject)
    except Exception as e:
        bad_request(e)


async def find_student_service(student_registration: str):
    try:
        return await find_student(student_registration)
    except Exception as e:
        bad_request(e)


async def find_professor_service(professor_registration: str):
    try:
        return await find_professor(professor_registration)
    except Exception as e:
        bad_request(e)


async def find_principal_service(principal_registration: str):
    try:
        return await find_professor(principal_registration)
    except Exception as e:
        bad_request(e)


async def find_subject_service(subject_id: str):
    try:
        return await find_subject(subject_id)
    except Exception as e:
        bad_request(e)


async def del_student_service(student_registration: str):
    try:
        await del_student(student_registration)
        await del_subject_student_notes(student_registration)
    except Exception as e:
        bad_request(e)


async def del_subject_service(subject_id: str):
    try:
        await del_subject(subject_id)
        await del_subject_notes(subject_id)
    except Exception as e:
        bad_request(e)


async def del_professor_service(professor_registration: str):
    try:
        await del_professor(professor_registration)
    except Exception as e:
        bad_request(e)
