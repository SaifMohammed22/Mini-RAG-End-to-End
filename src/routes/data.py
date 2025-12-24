"""
Dealing with files upload and validation
"""
from fastapi import FastAPI, APIRouter, Depends, UploadFile
from utils.config import get_settings, Settings
from controllers import DataController

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"]
)

@data_router.post('/upload/{project_id}')
async def upload_data(project_id: str, file: UploadFile,
                      app_settings: Settings = Depends(get_settings)):
    is_valid = DataController().validate_file(file=file)
    if is_valid:    
        return {"status": "File uploaded successfully", "project_id": project_id}
    return {"status": "File upload failed"}
