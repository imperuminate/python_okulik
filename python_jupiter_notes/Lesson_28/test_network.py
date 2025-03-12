from time import sleep
from playwright.sync_api import expect, Request, Page, APIResponse, Route
import re


def test_listen(page):

    def print_request(request: Request):
        print('REQUEST: ', request.post_data, request.url)

    page.on('request', print_request)
    page.on('response', lambda response: print(
        'RESPONSE:', response.url, response.status, response.text()))
    page.goto('https://www.qa-practice.com/')
    page.get_by_role('link', name='Text input').click()
    input_field = page.locator('#id_text_string')
    input_field.fill('dfdf')
    input_field.press('Enter')
    sleep(4)


def test_catch_response(page: Page):
    sleep(3)
    page.goto('https://www.airbnb.ru/')
    # with page.expect_response('**/autosuggestions**') as response_event:
    with page.expect_response(re.compile('autosuggestions')) as response_event:
        page.get_by_test_id('header-tab-search-block-tab-EXPERIENCES').click()

    response = response_event.value

    expect(APIResponse(response)).to_be_ok()
    print(response.url)
    print(response.status)
    response_data = response.json()
    assert response_data['show_nearby'] is False


def test_chache_response(page: Page):

    def handle_route(route: Route):
        body = {
            "city": "Минске",
            "temperature": "+322",
            "icon": "A2"
        }
        route.fulfill(json=body)

    def handle_route2(route: Route): # замена урлы при реквесте. Не сможет спросить погоду
        url = route.request.url
        url = url.replace('api/', '')
        route.continue_(url=url)

    page.route('**/pogoda/**', handle_route)
    page.goto('https://www.onliner.by/')
    page.locator('[name="query"]').click()
    sleep(30)


def test_change_request(page):
    def change_req(route: Route):
        url = route.request.url
        print(url)
        url = url.replace('filter3=15p01', 'filter3=15p04')
        route.continue_(url=url)
    page.route(re.compile('/product/finder/'), change_req)
    page.goto('https://www.samsung.com/au/smartphones/galaxy-z/')
    page.get_by_text('Below $500').click()
    sleep(45)


def test_api(page: Page): #плейрайт безполезен для чистого апи, он открывает браузер и тд. Лучше на чистом пайтесте все тестить. Но в юай тестах он полезен
    response = page.request.get('https://jsonplaceholder.typicode.com/posts/42')
    print(response.json(), response.status)
    expect(response).to_be_ok()
    assert response.json()['id'] == 42
    print(type(response))
