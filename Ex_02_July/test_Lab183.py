# Request module
# Post, Request, Put, Patch, Delete
# URL, Auth, Cookies, verification with Pytest.

# Get Request - Booking ID

# URL - https://restful-booker.herokuapp.com/booking/
# Auth
# Payload
# Content Type or Header
# Query Param
# Path param - yes - 1

# Response
# Body -> Verify - Assert, #keys, values
# Status code - Verify
# Time
# Json Schema

import pytest
import allure
import requests


@allure.title("Test GET Request - RestFul Booker Project #1")
@allure.description("TC1 -> Verify that Restful Booker GET ID works")
@allure.tag("regression", "P0", "smoke")
@allure.label("Owner", "Varun")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    print(response_data.json())
    assert response_data.status_code == 200


@allure.title("Test GET Request - RestFul Booker Project #2")
@allure.description("TC2 -> Verify that Get Request with invalid booking id")
@allure.tag("regression", "P0", "smoke")
@allure.label("Owner", "Varun")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_negative():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    response_data = requests.get(url)
    assert response_data.status_code == 404


@allure.title("Test GET Request - RestFul Booker Project #3")
@allure.description("TC3 -> Verify that Get Request with invalid booking id")
@allure.tag("regression", "P0", "smoke")
@allure.label("Owner", "Varun")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_negative1():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    response_data = requests.get(url)
    assert response_data.status_code != 404
