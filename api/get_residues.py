import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_URL = os.getenv("API_URL")
URL = f"{API_URL}/get-all-residue/"


def get_residues():
    try:
        response = requests.get(URL)
        return response.json()
    except Exception as e:
        return []
        print(e)