from fastapi import APIRouter
from UniSystem.domain.schemas import Dean, Principal, Professor


dean_routes = APIRouter(prefix='/dean')


@dean_routes.put('/professor/{professor_id}')
async def update_professor_salary(professor_id: int, new_professor_salary: Professor):
    return


@dean_routes.put('/principal')
async def update_principal_salary(new_principal_salary: Principal):
    return


@dean_routes.put("/account")
async def update_account(dean: Dean):
    return
