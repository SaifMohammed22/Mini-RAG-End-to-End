from controllers import BaseController
from fastapi import UploadFile, HTTPException

class DataController(BaseController):
    def __init__(self):
        super().__init__()
    
    def validate_file(self, file: UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            raise HTTPException(status_code=400, detail="Not allowed file extension. Allowed file types are: plain text, and pdf.")
        if file.size > self.app_settings.FILE_MAX_SIZE:
            raise HTTPException(status_code=400, detail="File size exceeds the allowed max size.")
        return True