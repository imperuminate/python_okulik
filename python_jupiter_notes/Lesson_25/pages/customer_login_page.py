from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from utils import project_ec
from pages.locators import customer_login_page_locators as locator



class CustomerLoginPage(BasePage):

    page_url = '/customer/account/login'

    def fill_login_form(self, email, password):
        email_input = self.find(locator.email_input_loc)
        password_input = self.find(locator.password_input_loc)
        send_button = self.find(locator.send_button_loc)
        email_input.send_keys(email)
        password_input.send_keys(password)
        send_button.click()


    def check_error_message(self, text):
        error_message = self.find(locator.error_message_loc)
        WebDriverWait(self.driver, 5).until(
            project_ec.text_is_not_empty_in_element(error_message))
        assert error_message.text == text
        print(error_message.text)
