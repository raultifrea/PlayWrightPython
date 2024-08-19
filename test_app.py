from playwright.sync_api import Page
import pytest

#Execute from CLI using pytest -v --headed --slowmo=500 --browser=chromium test_app.py 

DOCS_URL = 'https://playwright.dev/python/docs/intro'

@pytest.fixture
def playwrigt_page(page: Page):
    page.goto("https://playwright.dev/python/")
    return page

def test_page_has_get_docs_link(playwrigt_page: Page):

    link = playwrigt_page.locator('.getStarted_Sjon') 
    #same as page.get_by_role('link', name='Get started')    
    assert link.is_visible()

def test_page_has_get_started_visits_docs(playwrigt_page: Page):

    link = playwrigt_page.locator('.getStarted_Sjon') 
    link.click()
    
    assert playwrigt_page.url == DOCS_URL



@pytest.fixture(autouse=True, scope='function') #implicitly sets the scope to function
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
    link.click()
    assert page.url == DOCS_URL