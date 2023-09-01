from UniSystem.domain.schemas import *
from UniSystem.infra.querys.adds import *
from UniSystem.application.exceptions.http_exceptions import *


async def cad_professor_service(professor: Professor):
    try:
        professor_register_query(professor)
    except Exception as e:
        bad_request()


async def cad_student_service(student: Student):
    try:
        student_register_query(student)
    except Exception as e:
        bad_request()


async def cad_subject_service(subject: Subject):
    try:
        subject_register_query(subject)
    except Exception as e:
        bad_request()

