from playwright.sync_api import Page, expect
import pytest

BASE_URL = '127.0.0.1:8000'

@pytest.fixture(autouse=True)
def setup(page: Page):
    page.goto(BASE_URL)

def test_cube(page: Page):

    input = page.get_by_placeholder('enter number...')
    input.fill('5')

    page.get_by_role('button', name='Cube').click()

    result = page.locator('#result')

    expect(result).to_contain_text('125')

def test_empty_input(page: Page):
    input = page.get_by_placeholder('enter number...')
    input.fill('')

    page.get_by_role('button', name='Cube').click()

    result = page.locator('#result')

    expect(result).to_contain_text('Enter something!')