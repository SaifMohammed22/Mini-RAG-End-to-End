"""
The base routes file
"""
from fastapi import FastAPI, APIRouter, Depends
from utils import get_settings, Settings

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)

@base_router.get('/')
async def check_health(app_settings: Settings = Depends(get_settings)):
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return {
        'message': 'The backend is working',
        'app': f'{app_name}',
        'version': f'{app_version}',
        'status': 200
    }
