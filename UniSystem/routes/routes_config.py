from fastapi import FastAPI

from UniSystem.routes.actors_routes.security_routes import security_router
from UniSystem.routes.actors_routes.dean_routes import dean_router
from UniSystem.routes.actors_routes.principal_routes import principal_router
from UniSystem.routes.actors_routes.professor_routes import professor_router
from UniSystem.routes.actors_routes.students_routes import student_router
from UniSystem.routes.actors_routes.admin_routes import administrator_router


app = FastAPI()

app.include_router(security_router)
app.include_router(principal_router)
app.include_router(professor_router)
app.include_router(student_router)
app.include_router(dean_router)
app.include_router(administrator_router)
