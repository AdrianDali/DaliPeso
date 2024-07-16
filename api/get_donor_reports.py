import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_URL = os.getenv("API_URL")
URL = f"{API_URL}/get-all-donor-reports-user-container/"


def get_donor_reports(user):
    req = {
        "creator_user": user
    }
    try:
        response = requests.post(URL, data=req)
        return response.json()
    except Exception as e:
        print(e)
        return []