import pytest
import allure


@allure.title("TC#0 - Verify that 1-1 is equal to 0")
@allure.description("This is a smoke Testcase - Verify that 1-1 is equal to 0")
@pytest.mark.smoke
def test_sub():
    assert 1-1 == 0


@allure.title("TC#2 - Verify that 2-1 is equal to 1")
@allure.description("This is a regression Testcase - Verify that 2-1 is equal to 1")
@pytest.mark.regression
def test_sub_1():
    assert 2-1 == 1


@allure.title("TC#4 - Verify that 0-1 is equal to 1")
@allure.description("This is a regression Testcase - Verify that 0-1 is equal to 1")
@pytest.mark.regression
def test_sub_4():
    assert 0 - 1 == 1


@allure.title("TC#2 - Verify that 2-1 is not equal to 1")
@allure.description("This is a smoke Testcase - Verify that 2-1 is not equal to 1")
@pytest.mark.sanity
def test_sub_2():
    assert 2 - 1 != 1


@pytest.mark.skip
def test_sub_3():
    assert 1 - 0 == 1


