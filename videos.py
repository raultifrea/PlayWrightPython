from playwright.sync_api import Browser, Page
import pytest

DOCS_URL = 'https://playwright.dev/python/docs/intro'

@pytest.fixture(autouse=True)
def recordable(browser: Browser):
    context = browser.new_context(record_video_dir='videos/')
    page = context.new_page()
    yield page
    context.close()

def test_page_has_getstarted_link(page: Page):
    page.goto("https://playwright.dev/python/")

    theme_btn = page.locator('.toggleButton_gllP')
    theme_btn.wait_for(state="visible")
    theme_btn.click()

    link = page.locator('.getStarted_Sjon') 
    link.click()

    page.wait_for_url(DOCS_URL)
    assert page.url == DOCS_URL