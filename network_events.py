from models.playwright_page import PlaywrightPage
from playwright.sync_api import Route, Page

def on_route(route: Route):
    # route.request.post_data = 'data'
    if route.request.resource_type == 'image':
        print('Request aborted:', route.request)
        route.abort()
    else:
        route.continue_()

def on_route2(route: Route):
    response = route.fetch()
    body = response.text().replace(' enables reliable end-to-end testing for modern web apps.', " is an awesome framework!")
    route.fulfill(response=response, body=body)

def test_aborting_image_load(page: Page):
    page.route('**', on_route)

    homepage = PlaywrightPage(page)
    page.screenshot(path='pr.jpg', full_page=True)


def test_modify_response(page: Page):
    page.route('https://playwright.dev/python', on_route2)

    homepage = PlaywrightPage(page)
    page.screenshot(path='pr.jpg', full_page=True)

