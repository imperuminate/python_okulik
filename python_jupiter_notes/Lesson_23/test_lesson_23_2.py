# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import pytest

# from time import sleep


# @pytest.fixture()
# def driver():
#     chrome_driver = webdriver.Chrome()
#     chrome_driver.maximize_window()
#     yield chrome_driver
#     sleep(5)


# def test_id_name(driver):
#     input_data = "dsd"
#     driver.get("https://www.qa-practice.com/")
#     input_button = driver.find_element(By.XPATH, "//a[normalize-space()='Text input']")
#     input_button.click()
#     text_string = driver.find_element(By.NAME, "text_string")
#     text_string.send_keys(input_data)
#     text_string.send_keys(Keys.ENTER)
#     result_string = driver.find_element(By.ID, "result-text")
#     assert result_string.text == input_data


# def test_classname(driver):
#     input_data = "dsd"
#     driver.get("https://www.qa-practice.com/")
#     input_button = driver.find_element(By.XPATH, "//a[normalize-space()='Text input']")
#     input_button.click()
#     text_string = driver.find_element(By.CLASS_NAME, "textInput")
#     text_string.send_keys(input_data)
#     text_string.send_keys(Keys.ENTER)
#     result_string = driver.find_element(By.CLASS_NAME, "result-text")
#     assert result_string.text == input_data


# def test_tagname(driver):
#     driver.get("https://www.qa-practice.com/elements/input/simple")
#     header_text = driver.find_element(By.TAG_NAME, "h1")
#     assert header_text.text == "Input field"


# def test_link(driver):
#     driver.get("https://www.qa-practice.com/")
#     contact_link = driver.find_element(By.LINK_TEXT, "Contact")
#     contact_link = driver.find_element(By.PARTIAL_LINK_TEXT, "act")
#     contact_link.click()
#     header_text = driver.find_element(By.TAG_NAME, "h1")
#     assert header_text.text == "Contact us"


# def test_css(driver):
#     driver.get("https://www.qa-practice.com/elements/input/simple")
#     input_field = driver.find_element(By.CSS_SELECTOR, '[type="text"]')
#     print('**************************************** ',input_field.value_of_css_property('border'))
#     assert input_field.get_attribute('placeholder') == 'Submit me'


# def test_xpath(driver):
#     driver.get("https://www.qa-practice.com/elements/input/simple")
#     input_field = driver.find_element(By.XPATH, '//input[@placeholder="Submit me"]')


 
