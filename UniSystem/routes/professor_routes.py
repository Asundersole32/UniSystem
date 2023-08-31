from fastapi import APIRouter
from UniSystem.domain.schemas import Professor


professor_routes = APIRouter(prefix='/professor')


@professor_routes.put('/account')
async def update_account(professor: Professor):
    return


@professor_routes.post('/notes')
async def subject_note(subject_id: int, note: dict):
    return


@professor_routes.get('/notes/{subject_id}')
async def view_notes(subject_id: int):
    return


@professor_routes.get('/notes/{subject_id}')
async def notes_operation(operation: str, subject_id: int):
    return
