"""
The main app file
"""

from fastapi import FastAPI

app = FastAPI()

@app.get('/welcome')
def welcome():
    return {
        'message': "Hello! It's Saif."
    }

@app.get('/health')
def check_health():
    return {
        'message': 'The backend is working',
        'status': 200
    }
