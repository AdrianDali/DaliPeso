import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_URL = os.getenv("API_URL")
URL = f"{API_URL}/create-report-residue-user/"

def add_residue(user, report, residue, peso):
    req = {
    "user": "khfd@prueba.com",
    "report": "27",
    "residue": "PET",
    "peso": "1",
    "volumen": "3"
    }
    print(req)
    try:
        response = requests.post(URL, data=req)
        return response.json()
    except Exception as e:
        raise e