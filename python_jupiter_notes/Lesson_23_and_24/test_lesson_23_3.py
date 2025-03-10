# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import pytest
# from time import sleep


# @pytest.fixture()
# def driver():
#     chrome_driver = webdriver.Chrome()
#     # chrome_driver.implicitly_wait(6)
#     chrome_driver.maximize_window()
#     yield chrome_driver


# def test_clear(driver):
#     driver.get("https://www.qa-practice.com/elements/input/simple")
#     input_field = driver.find_element(By.CSS_SELECTOR, '[type="text"]')
#     input_field.send_keys('This is an input field')
#     sleep(1)
#     input_field.clear()
#     assert input_field.get_attribute('placeholder') == 'Submit me'

# def test_clear_if_clear_not_working(driver):
#     driver.get("https://www.qa-practice.com/elements/input/simple")
#     input_field = driver.find_element(By.CSS_SELECTOR, '[type="text"]')
#     input_field.send_keys('This is an input field')
#     sleep(1)
#     for _ in range(len(input_field.get_attribute("value"))):
#         input_field.send_keys(Keys.BACKSPACE)
#     assert input_field.is_displayed()


# def test_enebled_and_select(driver):
#     driver.get('https://www.qa-practice.com/elements/button/disabled')
#     submit_button = driver.find_element(By.NAME, 'submit')
#     print(submit_button.is_enabled())
#     dropdown_select = driver.find_element(By.CLASS_NAME, 'form-select')
#     dropdown = Select(dropdown_select)
#     dropdown.select_by_value('enabled')
#     print(submit_button.is_enabled())
#     assert submit_button.is_enabled()


# def test_vait(driver):
#     driver.get('https://demoqa.com/dynamic-properties')
#     button = driver.find_element(By.ID, 'visibleAfter')
#     assert button.is_displayed()


# def test_wait_card(driver):
#     driver.get('https://magento.softwaretestingboard.com/gabrielle-micro-sleeve-top.html')
#     size_button = driver.find_element(By.ID, 'option-label-size-143-item-166')
#     size_button.click()
#     color_button = driver.find_element(By.ID, 'option-label-color-93-item-58')
#     color_button.click()
#     add_button = driver.find_element(By.ID, 'product-addtocart-button')
#     add_button.click()
#     card_icon = driver.find_element(By.CLASS_NAME, 'counter-number')
#     wait = WebDriverWait(driver, 10)
#     wait.until_not(
#         EC.text_to_be_present_in_element_attribute(
#             (By.CSS_SELECTOR, ".counter.qty"), "class", "empty"
#         )
#     )
#     wait.until_not(
#         EC.text_to_be_present_in_element_attribute(
#             (By.CSS_SELECTOR, ".counter.qty"), "class", "loading"
#         )
#     )
#     print(card_icon.text, '*******************************************************')
#     assert card_icon.text == '1'


# def test_vait_explicitly(driver):
#     driver.get('https://demoqa.com/dynamic-properties')
#     WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.ID, 'visibleAfter')))
#     button = driver.find_element(By.ID, 'visibleAfter')
#     driver.delete_all_cookies()
#     driver.add_cookie({'name': 'testname', 'value': 'testvalue'})
#     print(driver.get_cookies())
#     assert button.is_displayed()


# def test_a_lot_of_same_elements(driver):
#     driver.get('https://magento.softwaretestingboard.com/women/bottoms-women/shorts-women.html')
#     produkt_link = driver.find_elements(By.CLASS_NAME, 'product-item-link')
#     print(produkt_link[0].text)
#     sleep(1)
#     print(produkt_link[-1].text)


# def test_element_in_element(driver):
#     driver.get('https://magento.softwaretestingboard.com/women/bottoms-women/shorts-women.html')
#     produkt_link = driver.find_elements(By.CLASS_NAME, 'product-item-info')
#     for card in produkt_link:
#         print(card.find_element(By.CLASS_NAME, 'price').text)
#     sleep(1)
# # можно проверять сортировку в товаров применив фильтр по цене
