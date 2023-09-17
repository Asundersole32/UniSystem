from UniSystem.domain.schemas import *
from UniSystem.infra.querys.adds import *
from UniSystem.infra.querys.consult import *
from UniSystem.application.exceptions.http_exceptions import *


async def cad_professor_service(professor: Professor):
    try:
        await professor_register_query(professor)
    except Exception as e:
        bad_request()


async def cad_student_service(student: Student):
    try:
        await student_register_query(student)
    except Exception as e:
        bad_request()


async def cad_subject_service(subject: Subject):
    try:
        await subject_register_query(subject)
    except Exception as e:
        bad_request()


async def find_student_service(student_registration: str):
    try:
        return await find_student(student_registration)
    except Exception as e:
        print(e)
        bad_request()


async def find_professor_service(professor_registration: str):
    try:
        return await find_professor(professor_registration)
    except Exception as e:
        print(e)
        bad_request()


async def find_principal_service(principal_registration: str):
    try:
        return await find_professor(principal_registration)
    except Exception as e:
        bad_request()


async def find_subject_service(subject_id: str):
    try:
        return await find_subject(subject_id)
    except Exception as e:
        bad_request()
