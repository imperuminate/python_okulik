import re
from time import sleep
from playwright.sync_api import expect, Dialog


# def test_visible(page):
#     page.goto('https://www.qa-practice.com/elements/button/disabled')
#     text_block = page.locator('.card-body')
#     expect(text_block).not_to_be_visible()
#     page.get_by_role('button', name='Requirements:').click()
#     print(text_block)
#     expect(text_block).to_be_visible()


# def test_select_and_disabled(page):
#     page.goto('https://www.qa-practice.com/elements/button/disabled')
#     select_button = page.locator('.form-select')
#     select_button.select_option('Enabled')
#     submit_button = page.locator('.btn.btn-primary')
#     expect(submit_button).to_be_enabled()
#     expect(submit_button, 'It\'s expected to by disabled. But its enabled'
#            ).to_be_disabled() # как добавить комента пояснение на случай падения теста



# def test_have_exact_text(page):
#     page.goto('https://www.qa-practice.com/elements/button/disabled')
#     select_button = page.locator('.form-select')
#     select_button.select_option('Enabled')
#     submit_button = page.locator('.btn.btn-primary')
#     expect(submit_button).to_have_text('Submit')


# def test_contain_text(page):
#     page.goto('https://www.qa-practice.com/elements/button/disabled')
#     select_button = page.locator('.form-select')
#     select_button.select_option('Enabled')
#     submit_button = page.locator('.btn.btn-primary')
#     expect(submit_button).to_contain_text('ubmi')

# def test_field_have_value(page):
#     page.goto('https://www.qa-practice.com/elements/input/simple')
#     input_field = page.get_by_placeholder('Submit me')
#     input_field.fill('https://www.qa-practice.com/elements/input/simple')
#     expect(input_field).to_have_value('https://www.qa-practice.com/elements/input/simple')


# def test_sort_and_waits(page):
#     page.goto('https://magento.softwaretestingboard.com/women/bottoms-women/shorts-women.html')
#     first_item = page.locator('.product-item-link').locator('nth=0')
#     sleep(1)
#     expect(first_item).not_to_be_empty()
#     print(first_item.inner_text(), "**************************")
#     items_sort_button = page.locator('#sorter').locator('nth=0')
#     items_sort_button.select_option('Price')
#     expect(page).to_have_url(re.compile('price'))
#     print(first_item.inner_text(), "**************************")


# def test_focused(page):
#     page.goto('https://www.google.com')
#     field = page.locator('[name="q"]')
#     sleep(3)
#     expect(field).to_be_focused()


# def test_tabs(page, context):
#     page.goto('https://www.qa-practice.com/elements/new_tab/link')
#     link = page.locator('#new-page-link')
#     with context.expect_page() as new_page_event:
#         link.click()
#     new_page = new_page_event.value
#     new_page_text = new_page.locator('.result-text')
#     expect(new_page_text).to_have_text('I am a new page in a new tab')
#     page.get_by_text('New tab button').click()
#     page.locator('.a-button').click()
#     new_page.close()
#     sleep(4)
#     # context - это браузер
#     # page - это вкладка в браузере


# def test_hover(page):
#     page.goto('https://magento.softwaretestingboard.com')
#     man = page.locator('#ui-id-5')
#     tops = page.locator('#ui-id-17')
#     jackets = page.locator('#ui-id-19')
#     man.hover()
#     tops.hover()
#     jackets.click()
#     sleep(4)

# def test_drag_and_drop(page):
#     page.goto('https://www.qa-practice.com/elements/dragndrop/boxes')
#     box = page.locator('.ui-draggable-handle')
#     area = page.locator('.rect-droppable.ui-droppable')
#     box.drag_to(area)
#     sleep(4)


def test_alert(page):
    page.goto('https://www.qa-practice.com/elements/alert/prompt')
    # def alert_cancel(alert: Dialog):
    #     print(alert.message)
    #     print(alert.type)
    #     alert.dismiss()
    # def alert_accept(alert: Dialog):
    #     print(alert.message, '*******************')
    #     print(alert.type, '*******************')
    #     alert.accept('https')
    # page.on('dialog', alert_accept)
    page.on('dialog', lambda alert: alert.accept('https'))
    page.get_by_role('link', name='Click').click()
    sleep(3)
