import pytest
import allure
import requests


@allure.title("Create Booking CRUD")
@allure.description("#TC1 Verify the create Booking")
@pytest.mark.crud
def test_create_booking_positive():
    # To make Request
    # URL
    # Method POST
    # Headers - Content-Type: application/json
    # Payload / body - Dict / JSON
    # Auth(no)

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
    assert response.status_code == 200
    response = response.json()
    assert response["bookingid"] is not None
    assert type(response["bookingid"]) == int




