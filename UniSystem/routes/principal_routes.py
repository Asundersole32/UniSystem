from UniSystem.domain.schemas import Student, Professor, Subject, Principal
from UniSystem.application.services.principal_services import *
from fastapi import APIRouter


principal_routers = APIRouter(prefix='/principal')


@principal_routers.put('/account')
async def update_account(principal: Principal):
    return


@principal_routers.post('/professor')
async def cad_professor(professor: Professor):
    cad = await cad_professor_service(professor)
    return cad


@principal_routers.post('/students')
async def cad_student(student: Student):
    return


@principal_routers.post('/subject')
async def cad_subject(subject: Subject):
    return


@principal_routers.delete('/professor/{professor_id}')
async def del_professor(professor_id: int):
    return


@principal_routers.delete('/student/{student_id}')
async def del_student(student_id: int):
    return


@principal_routers.delete('/subject/{subject_id}')
async def del_subject(subject_id: int):
    return


@principal_routers.get('/professor/{professor_id}')
async def get_professor(professor_id: int):
    return


@principal_routers.get('/student/{student_id}')
async def get_student(student_id: int):
    return


@principal_routers.put('/professor/{professor_id}')
async def update_professor(professor_id: int, professor: Professor):
    return


@principal_routers.put('/students/{student_id}')
async def update_student(student_id: int, student: Student):
    return


@principal_routers.put('subjects/{subjects_id}')
async def update_subjects(subject_id: int, subjects: Subject):
    return
