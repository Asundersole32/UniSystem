from UniSystem.util.init_db import create_database, academic_type_insert
from UniSystem.routes.professor_routes import professor_routes
from UniSystem.routes.dean_routes import dean_routes
from UniSystem.routes.principal_routes import principal_routers
from UniSystem.routes.students_routes import student_routes
from asyncio import run
from fastapi import FastAPI
import uvicorn
import os
import logging


'''run(create_database())
run(academic_type_insert())'''

app = FastAPI()
app.include_router(principal_routers)
app.include_router(professor_routes)
app.include_router(student_routes)
app.include_router(dean_routes)
