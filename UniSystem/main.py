from UniSystem.routes.routes_config import app
from UniSystem.util.init_db import create_database, academic_type_insert
import uvicorn
import os
import logging
from asyncio import run


def start():

    uvicorn.run(
        app,
        port=int(os.getenv("API_PORT", "8000")),
        host=os.getenv("API_HOST", "localhost"),
        log_level=logging.DEBUG
    )


'''run(create_database())
run(academic_type_insert())'''
start()
