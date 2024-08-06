# Fixture
# Giving context to the test
# Pre- or post-condition
# For update - we need to create token and booking
# This can be done through fixture
import pytest
import requests


def test_update_request_1(create_token, create_booking):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = f"/booking/{create_booking}"
    url = base_url + base_path
    headers = {"Content-Type": "application/json",
               "cookie": f"token={create_token}"
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
