import pytest
import requests
from data.urls import Urls
import os
from dotenv import load_dotenv

load_dotenv()
urls = Urls()


username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")




@pytest.fixture(scope="session")
def authorized():
    data = {
        "userName" : username,
        "password" : password
    }
    response = requests.post(urls.API.AUTHORIZED, json=data)
    #token = response.json()["token"]
    # return response.json(), data['username'], data['password']
    return response




