from fastapi import APIRouter
from UniSystem.domain.schemas import Dean, Principal, Professor


dean_router = APIRouter(prefix='/dean')


@dean_router.put('/professor/{professor_id}')
async def update_professor_salary(professor_id: int, new_professor_salary: Professor):
    return


@dean_router.put('/principal')
async def update_principal_salary(new_principal_salary: Principal):
    return


@dean_router.put("/account")
async def update_account(dean: Dean):
    return


@dean_router.post('/principal')
async def principal_register(principal: Principal):
    return
