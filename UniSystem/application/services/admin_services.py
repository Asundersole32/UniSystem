from UniSystem.util.init_db import *
from UniSystem.application.exceptions.http_exceptions import bad_request
from UniSystem.domain.schemas import Academic
from UniSystem.infra.querys.adds import admin_register_query


def admin_dict_to_base(admin_dict):
    admin = Academic
    admin.registration = admin_dict['registration']
    admin.name = admin_dict['name']
    admin.institutional_email = admin_dict['institutional_email']
    admin.password = '123456'
    return admin


async def admin_register_service(admin: Academic):
    try:
        await admin_register_query(admin)
        return {'response': True}
    except Exception as e:
        bad_request(e)


async def init_db_service():
    try:
        await create_database()
        await academic_type_insert()
        return {'response': True}
    except Exception as e:
        bad_request(e)


async def find_admins():
    admins = await find_admins()
    return admins
