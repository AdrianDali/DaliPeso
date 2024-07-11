import os
from urllib import response
from dotenv import load_dotenv
import requests

load_dotenv()

API_URL = os.getenv("API_URL")
LOGIN_URL = f"{API_URL}/api/token/"


def login(req):
    try:
        response = requests.post(LOGIN_URL, data=req)
        return response.json()
    except Exception as e:
        print(e)