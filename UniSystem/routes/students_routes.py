from fastapi import APIRouter
from UniSystem.domain.schemas import Student

student_routes = APIRouter(prefix='/students')


@student_routes.put('/account')
async def update_account(student: Student):
    return


@student_routes.get('/notes')
async def view_notes():
    return


@student_routes.get('/subjects')
async def view_subjects():
    return


@student_routes.put('/vote')
async def principal_vote(vote: int):
    return
