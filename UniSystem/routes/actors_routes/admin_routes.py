from fastapi import APIRouter
from asyncio import run

from UniSystem.application.services.admin_services import *
from UniSystem.application.security import *


administrator_router = APIRouter(prefix='/admin',
                                 tags=['admin'])


@administrator_router.get('/init_db')
async def init_db(user: Annotated[User, Depends(get_current_user)]):
    if user['academic_type_id'] == 5:
        init = await init_db_service()
        admin = admin_dict_to_base(user)
        cad = await admin_register_service(admin)
        return {'init': init, 'cad': cad, 'temp password': '123456'}
    else:
        admins = await find_admins()
        if not admins:
            init = await init_db_service()



@administrator_router.post('')
async def administrator_registrator(admin: Academic):
    return await admin_register_service(admin)
