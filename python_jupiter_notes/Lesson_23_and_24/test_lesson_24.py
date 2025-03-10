from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import pytest
from time import sleep



@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver



# def test_new_tab_switch(driver):
#     driver.get("https://www.qa-practice.com/elements/new_tab/link")
#     new_tab_button = driver.find_element(By.ID, 'new-page-link')
#     new_tab_button.click()
#     tabs = driver.window_handles
#     print(tabs)
#     driver.switch_to.window(tabs[1])
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'result-text')))
#     new_tab_text = driver.find_element(By.CLASS_NAME, 'result-text')
#     assert new_tab_text.text == 'I am a new page in a new tab'
#     driver.close()
#     driver.switch_to.window(tabs[0])
#     assert new_tab_button.is_enabled()


# def test_iframe(driver):
#     driver.get("https://www.qa-practice.com/elements/iframe/iframe_page")
#     iframe = driver.find_element(By.CLASS_NAME, 'embed-responsive-item')
#     driver.switch_to.frame(iframe)
#     burger_menu = driver.find_element(By.CLASS_NAME, 'navbar-toggler-icon')
#     burger_menu.click()
#     sleep(1)
#     driver.switch_to.default_content()
#     home_button = driver.find_element(By.XPATH, '//a[@href="/"]')
#     home_button.click()
#     print(home_button.text)
#     sleep(5)


# def test_dropdown_menu(driver):
#     driver.get('https://magento.softwaretestingboard.com/')
#     women = driver.find_element(By.ID, 'ui-id-4')
#     tops = driver.find_element(By.ID, 'ui-id-9')
#     jacket = driver.find_element(By.ID, 'ui-id-11')
#     # ActionChains(driver).move_to_element(women).move_to_element(tops).click(jacket).perform()
#     actions = ActionChains(driver)
#     actions.move_to_element(women)
#     actions.move_to_element(tops)
#     actions.click(jacket)
#     actions.perform()
#     actions.double_click(women)
#     actions.context_click(women)
#     sleep(5)


# def test_draf_and_drop(driver):
#     driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
#     box = driver.find_element(By.ID, 'rect-draggable')
#     area_for_box = driver.find_element(By.ID, 'rect-droppable')
#     actions = ActionChains(driver)
#     actions.drag_and_drop(box, area_for_box).perform()
#     # actions.click_and_hold(box)
#     # actions.move_to_element(area_for_box)
#     # actions.release()
#     # actions.perform()
#     sleep(4)


# def test_open_in_new_tab(driver):
#     driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
#     link = driver.find_element(By.LINK_TEXT, 'Homepage')
#     ActionChains(driver).key_down(Keys.COMMAND).click(link).key_up(Keys.COMMAND).perform() 
#     sleep(3)


def test_alerts(driver):
    driver.get('https://www.qa-practice.com/elements/alert/prompt')
    allert_button = driver.find_element(By.CLASS_NAME, 'a-button')
    allert_button.click()
    alert = Alert(driver)
    alert.send_keys('Hi, am tired')
    sleep(1)
    alert.accept()
    sleep(3)