from playwright.sync_api import Page
import pytest

#Execute from CLI using pytest -v --headed --slowmo=500 --browser=chromium test_app.py 

DOCS_URL = 'https://playwright.dev/python/docs/intro'

@pytest.fixture
def playwrigt_page(page: Page):
    page.goto("https://playwright.dev/python/")
    page.screenshot(path='playwright.png')
    return page

def test_page_has_get_docs_link(playwrigt_page: Page):

    link = playwrigt_page.locator('.getStarted_Sjon') 
    #same as page.get_by_role('link', name='Get started')    
    assert link.is_visible()

def test_page_has_get_started_visits_docs(playwrigt_page: Page):

    link = playwrigt_page.locator('.getStarted_Sjon') 
    link.click()
    playwrigt_page.screenshot(path='docs.jpg', full_page=True) #full scrollable page

    assert playwrigt_page.url == DOCS_URL


@pytest.fixture(autouse=True, scope='function') #implicitly sets the scope to function, we don't need to use the visit_playwright function as a parameter, it wil lbe automatically used in the below tests
def visit_playwright(page: Page):
    page.goto("https://playwright.dev/python/")
    yield page
    page.close()
    print('\n[ Fixture ]: page closed!')

def test_page_has_get_docs_link_hook(page: Page):
    link = page.locator('.getStarted_Sjon') 
    #same as page.get_by_role('link', name='Get started')    
    assert link.is_visible()

def test_page_has_get_started_visits_docs_hook(page: Page):
    link = page.locator('.getStarted_Sjon') 
    link.screenshot(path='getStarted.jpg') #take screenshot of specific locator
    link.click()
    
    assert page.url == DOCS_URL

def test_scroll_to_botton_using_JS_exec(page: Page):
    page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
    page.screenshot(path='end.jpg')
