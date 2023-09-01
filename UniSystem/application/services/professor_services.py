from UniSystem.domain.schemas import SubjectNote
from UniSystem.application.exceptions.http_exceptions import *
from UniSystem.infra.querys.adds import subject_notes_register_query


async def subject_notes_cad_service(subnote: SubjectNote):
    try:
        subject_notes_register_query(subnote)
    except Exception as e:
        bad_request()
