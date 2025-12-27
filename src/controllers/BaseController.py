import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils import get_settings
import random
import string

class BaseController:
    def __init__(self):
        self.app_settings = get_settings()
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.files_dir = os.path.join(self.base_dir, 'assets/files')
    
    def generate_random_string(self, length=8):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(length))

if __name__ == "__main__":
    base = BaseController()
    print(base.base_dir)
    print(base.files_dir)