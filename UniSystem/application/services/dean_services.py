from UniSystem.infra.querys.adds import *
from UniSystem.application.exceptions.http_exceptions import bad_request
from UniSystem.domain.schemas import *


async def principal_register_service(principal: Principal):
    try:
        await principal_register_query(principal)
    except Exception as e:
        bad_request(e)

