from playwright.sync_api import Page, expect
import re
from time import sleep


def test_one(page: Page): # Test will not work due to google captcha
    page.goto('https://www.google.com/')
    search_field = page.get_by_role('combobox')
    search_field.fill('cat')
    search_field.press('Enter')
    expect(page).to_have_title(re.compile('^cat')) # cat at the begining
    expect(page).to_have_title(re.compile('cat$')) # cat at the end
    expect(page).to_have_title(re.compile('cat')) # cat somewhere in the text


def test_by_role(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    button = page.get_by_role('menuitem', name="What's New")
    sleep(2)
    button.click()
    sleep(3)


def test_by_text(page):
    page.goto('https://www.qa-practice.com/')
    page.get_by_text('Single UI Elements').click()
    sleep(3)


def test_by_label(page): #по заголовку который над полем. не в самом поле. 
    page.goto('https://www.qa-practice.com/elements/input/simple')
    page.get_by_label('Text string*').fill('Hello')
    sleep(3)


def test_by_placeholder(page): 
    sleep(3)
    page.goto('https://www.qa-practice.com/elements/input/simple')
    field = page.get_by_label('Text string')
    field.press_sequentially('ksjdfhksjdfh', delay=500)
    sleep(1)
    field.press('Meta+a') #Meta это cmd или control на винде
    sleep(1)
    field.press('Backspace')
    sleep(3)


def test_by_alt_text(page):
    page.goto('https://epam.com')
    page.get_by_alt_text('The Next Evolution of Software Engineering').click()
    sleep(3)


def test_by_title(page):
    page.goto('https://www.google.com/')
    page.get_by_title('Шукаць').fill('cat')
    sleep(3)

def test_by_testid(page):
    page.goto('https://www.airbnb.com/')
    page.get_by_test_id('header-tab-search-block-tab-EXPERIENCES').click()
    sleep(4)


def test_by_css(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    page.locator('.showcart').click()
    sleep(3)
 

def test_by_xpath(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    page.locator('//*[@class="action showcart"]').click()
    sleep(3)