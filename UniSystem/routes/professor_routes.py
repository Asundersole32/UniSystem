from fastapi import APIRouter
from UniSystem.domain.schemas import Professor


professor_router = APIRouter(prefix='/professor')


@professor_router.put('/account')
async def update_account(professor: Professor):
    return


@professor_router.post('/notes')
async def subject_note(subject_id: int, note: dict):
    return


@professor_router.get('/notes/{subject_id}')
async def view_notes(subject_id: int):
    return


@professor_router.get('/notes/{subject_id}')
async def notes_operation(operation: str, subject_id: int):
    return
