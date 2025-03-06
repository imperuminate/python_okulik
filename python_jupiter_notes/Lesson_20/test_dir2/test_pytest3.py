import pytest
import allure


@allure.feature("Example")
@pytest.fixture()
def num():
    return 1

@allure.feature("Example")
def test_num(num):
    print(num)