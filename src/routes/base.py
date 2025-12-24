"""
The base routes file
"""
import os
from fastapi import FastAPI, APIRouter

# Load env variables from .env
APP_NAME = os.getenv("APP_NAME") 
APP_VERSION = os.getenv("APP_VERSION") 

base_router = APIRouter(
    prefix="/api/v_1",
    tags=["api_v1"]
)

@base_router.get('/')
def check_health():
    return {
        'message': 'The backend is working',
        'app': f'{APP_NAME}',
        'version': f'{APP_VERSION}',
        'status': 200
    }
