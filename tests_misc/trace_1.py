from playwright.sync_api import BrowserContext, Page
import pytest

DOCS_URL = 'https://playwright.dev/python/docs/intro'

@pytest.fixture(autouse=True)
def trace_test(context: BrowserContext):
    context.tracing.start(name='playwright', screenshots=True, snapshots=True, sources=True)
    yield
    context.tracing.stop(path='trace.zip')

def test_page_has_get_started_visits_docs(page: Page):
    page.goto("https://playwright.dev/python/")

    link = page.locator('.getStarted_Sjon') 
    link.click()
    page.screenshot(path='docs.jpg', full_page=True) #full scrollable page

    assert page.url == DOCS_URL