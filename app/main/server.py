import logging

from fastapi import FastAPI
from fastapi.logger import logger as fastapi_logger

from app.main.routes import account_routes


gunicorn_error_logger = logging.getLogger("gunicorn.error")
gunicorn_logger = logging.getLogger("gunicorn")
uvicorn_access_logger = logging.getLogger("uvicorn.access")
uvicorn_access_logger.handlers = gunicorn_error_logger.handlers

fastapi_logger.handlers = gunicorn_error_logger.handlers

app = FastAPI(title='FastAPI Crud', version='1.0.0')

app.include_router(account_routes.router, prefix='/api')

if __name__ != "__main__":
    fastapi_logger.setLevel(gunicorn_logger.level)
else:
    fastapi_logger.setLevel(logging.DEBUG)
