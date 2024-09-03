from playwright.sync_api import Page, Route
import pytest

#Run individual test from this file: pytest -k test_page_has_get_docs_link intercept_requests.py 

@pytest.fixture
def browser_context_args():
    return {
        "java_script_enabled": False
    }

DOCS_URL = 'https://playwright.dev/python/docs/intro'
NOT_ALLOWED_RESOURCES = (
    "image", 'font', 'stylesheets', 'media', 'script'
)

def on_route(route: Route):
    if route.request.resource_type in NOT_ALLOWED_RESOURCES:
        route.abort()
    else:
        route.continue_()

@pytest.fixture
def playwright_page(page: Page):
    page.route('**', on_route)
    page.goto("https://playwright.dev/python/")
    return page

def test_page_has_get_docs_link(playwright_page: Page):
    link = playwright_page.locator('.getStarted_Sjon')
    # breakpoint() #to enter Python debugger console to interact from this point
    assert link.is_visible()

def test_page_has_get_started_visits_docs(playwright_page: Page):

    link = playwright_page.locator('.getStarted_Sjon') 
    link.click()

    assert playwright_page.url == DOCS_URL