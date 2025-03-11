import pytest
from selenium import webdriver
from pages.customer_login_page import CustomerLoginPage
from pages.sale_page import SalePage


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


@pytest.fixture()
def customer_login_page(driver):
    return CustomerLoginPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)