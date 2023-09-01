from UniSystem.routes.professor_routes import professor_router
from UniSystem.routes.dean_routes import dean_router
from UniSystem.routes.principal_routes import principal_router
from UniSystem.routes.students_routes import student_router
from UniSystem.util.init_db import *
from asyncio import run
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated


'''run(create_database())
run(academic_type_insert())'''

app = FastAPI()
app.include_router(principal_router)
app.include_router(professor_router)
app.include_router(student_router)
app.include_router(dean_router)





