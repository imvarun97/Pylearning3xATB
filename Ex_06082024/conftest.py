# This file will be automatically recognised by pytest
# so the fu

import pytest
import requests

@pytest.fixture()
def create_token():
    url = 'https://restful-booker.herokuapp.com/auth'
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()['token']
    return token


@pytest.fixture()
def create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=url, headers=headers, json=payload)
    booking_id = response.json()['bookingid']
    return booking_id