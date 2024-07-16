import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_URL = os.getenv("API_URL")
URL = f"{API_URL}/create-report-residue-user/"

def add_residue(user, report, residue, peso):
    arr = []
    req = {
        "user": user,
        "report": report,
        "residue": residue,
        "peso": peso,
        "volumen": "3"  # Make sure to adjust this if it's a dynamic value
    }
    arr.append(req)
    print(req)
    try:
        response = requests.post(URL, json=arr)
        return response.json()
    except Exception as e:
        raise e