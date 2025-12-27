import os
from .BaseController import BaseController
from .ProjectController import ProjectController
from fastapi import UploadFile, HTTPException
from models import ResponseSignal
import re

class DataController(BaseController):
    def __init__(self):
        super().__init__()
    
    def validate_file(self, file: UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            raise HTTPException(status_code=400, detail="Not allowed file extension. File should be: plain text, and pdf.")
        if file.size > self.app_settings.FILE_MAX_SIZE:
            raise HTTPException(status_code=400, detail="File size exceeds the allowed max size.")
        return True, ResponseSignal.FILE_UPLOAD_SUCCESS.value

    def generate_unique_filename(self, original_filename: str, project_id: str) -> str:
        random_key = self.generate_random_string(12)
        
        project_controller = ProjectController()
        proj_path = project_controller.get_project_path(project_id=project_id)
        clean_filename = self.get_clean_filename(original_filename)
        new_file_path = os.path.join(proj_path, random_key + "_" + clean_filename)
        
        while os.path.exists(new_file_path):
            random_key = self.generate_random_string(12)
            new_file_path = os.path.join(proj_path, random_key + "_" + clean_filename)

        return new_file_path

    def get_clean_filename(self, filename: str) -> str:
        clean_name = re.sub(r'[^\w.]', '', filename.strip())
        clean_name = clean_name.replace(' ', '_')
        return clean_name
