from UniSystem.domain.schemas import Student, Professor, Subject
from UniSystem.application.exceptions.http_exceptions import unauthorized_access
from UniSystem.application.services.principal_services import *
from UniSystem.application.security import *

from fastapi import APIRouter, Depends
from typing import Annotated


principal_router = APIRouter(prefix='/principal',
                             tags=['Principal'])


@principal_router.put('/account')
async def update_account(field: str, new_value, user: Annotated[User, Depends(get_current_user)]):
    if user['academic_type_id'] == 2:
        update = update_account_service(user['registration'], field, new_value)
        return update
    else:
        unauthorized_access()


@principal_router.post('/professor')
async def register_professor(professor: Professor, user: Annotated[User, Depends(get_current_user)]):
    if user['academic_type_id'] == 2 or user['academic_type_id'] == 5:
        cad = await cad_professor_service(professor)
        return cad
    else:
        unauthorized_access()


@principal_router.post('/students')
async def register_student(student: Student):
    cad = await cad_student_service(student)
    return cad


@principal_router.post('/subject')
async def register_subject(subject: Subject):
    cad = await cad_subject_service(subject)
    return cad


@principal_router.delete('/professor/{professor_id}')
async def del_professor(professor_id: str):
    delt = del_professor_service(professor_id)
    return delt


@principal_router.delete('/student/{student_id}')
async def del_student(student_id: str):
    delt = del_student_service(student_id)
    return delt


@principal_router.delete('/subject/{subject_id}')
async def del_subject(subject_id: str):
    delt = del_subject_service(subject_id)
    return delt


@principal_router.get('/professor/{professor_id}')
async def get_professor(professor_id: str):
    get = await find_professor_service(professor_id)
    return get


@principal_router.get('/student/{student_id}')
async def get_student(student_id: str):
    get = await find_student_service(student_id)
    return get


@principal_router.get('/subject/{subject_id}')
async def get_subject(subject_id: str):
    get = await find_subject_service(subject_id)
    return get


@principal_router.get('/principal/{principal_id}')
async def get_principal(principal_id: str):
    get = await find_principal_service(principal_id)
    return get



@principal_router.put('/professor/{professor_id}')
async def update_professor(professor_id: str, field: str, value):
    return


@principal_router.put('/students/{student_id}')
async def update_student(student_id: str, field: str, value):
    return


@principal_router.put('subjects/{subjects_id}')
async def update_subjects(subject_id: int, field: str, value):
    return
