from fastapi import FastAPI

from UniSystem.routes.dean_routes import dean_router
from UniSystem.routes.principal_routes import principal_router
from UniSystem.routes.professor_routes import professor_router
from UniSystem.routes.students_routes import student_router


app = FastAPI()

app.include_router(principal_router)
app.include_router(professor_router)
app.include_router(student_router)
app.include_router(dean_router)
