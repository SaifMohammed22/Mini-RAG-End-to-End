"""
Dealing with files upload and validation
"""
from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from utils import get_settings, Settings
from controllers import DataController
from models import ResponseSignal
import aiofiles
from logging import getLogger

logger = getLogger("uvicorn.error")


data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"]
)

@data_router.post('/upload/{project_id}')
async def upload_data(project_id: str, file: UploadFile,
                      app_settings: Settings = Depends(get_settings)):
    
    data_controller = DataController()

    is_valid, result_message = data_controller.validate_file(file=file)
    if not is_valid:    
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content= {
                "message": result_message
            }
        )
    
    file_path = data_controller.generate_unique_filename(original_filename=file.filename, project_id=project_id)

    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:

        logger.error(f"Error while uploading file: {e}")

        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResponseSignal.FILE_UPLOAD_FAILED.value
            }
        )

    return {"status": ResponseSignal.FILE_UPLOAD_SUCCESS.value}
