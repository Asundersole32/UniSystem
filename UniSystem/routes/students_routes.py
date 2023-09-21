from fastapi import APIRouter
from UniSystem.domain.schemas import Student

student_router = APIRouter(prefix='/students',
                           tags=['Students'])


@student_router.put('/account')
async def update_account(student: Student):
    return


@student_router.get('/notes')
async def view_notes():
    return


@student_router.get('/subjects')
async def view_subjects():
    return


@student_router.put('/vote')
async def principal_vote(vote: int):
    return
