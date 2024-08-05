# PUT
# URL
# PATH

import pytest
import allure
import requests


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
    booking_id = response.json()['booking_id']
    return booking_id


def test_put_request():
    token = create_token()
    booking_id = create_booking()

    base_url = "https://restful-booker.herokuapp.com"
    base_path = f"/booking/{booking_id}"
    url = base_url + base_path
    headers = {"Content-Type": "application/json",
               "cookie": f"token={token}"
               }
    payload = {
        "firstname": "Varun",
        "lastname": "Na",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=url, headers=headers, json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["firstname"] == 'Varun'




