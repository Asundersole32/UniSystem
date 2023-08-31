from UniSystem.domain.schemas import Professor
from UniSystem.infra.postgres.connection import async_session
from UniSystem.infra.postgres.tables import Professors
from UniSystem.application.security import get_hash_password
from fastapi import HTTPException, status


async def cad_professor_service(professor: Professor):
    try:
        hashed_password = get_hash_password(professor.password)
        professor.academic_type_id = 2
        professor.professional_status = 'professor'
        async with async_session() as session:
            session.add(Professors(registration=professor.registration, name=professor.name,
                                   registration_date=professor.registration_date,
                                   institutional_email=professor.institutional_email, password=hashed_password,
                                   academic_type_id=professor.academic_type_id,
                                   academic_formation=professor.academic_formation,
                                   academic_status=professor.academic_status,
                                   professional_status=professor.professional_status,
                                   salary=professor.salary, academic_training_place=professor.academic_training_place))
            await session.commit()
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST
        )
        