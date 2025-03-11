from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import sale_page_locators as locator


class SalePage(BasePage):
    page_url = '/sale.html'

    def check_header(self, header_text):
        header = self.find(locator.header_loc)
        assert header.text == header_text
