from dotenv import load_dotenv
import sys
import os


def env_connection_values(value):
    path = '../config/.env'
    load_dotenv(path)

    value_content = os.getenv(value)
    return value_content
