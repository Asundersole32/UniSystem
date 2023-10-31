from UniSystem.routes.routes_config import app
import uvicorn
import os
import logging


def start():

    uvicorn.run(
        app,
        port=int(os.getenv("API_PORT", "8000")),
        host=os.getenv("API_HOST", "localhost"),
        log_level=logging.DEBUG
    )


start()
