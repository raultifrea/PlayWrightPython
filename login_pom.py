from models.login_page import LoginPage
from playwright.sync_api import Page, expect

def test_successful_login(page: Page):
    username = 'Raul'
    password = 'pwd'

    login_page = LoginPage(page)
    login_page.login(username, password)

    expect(login_page.login_status).to_have_text(f'Welcome, {username}!')

def test_failed_login(page: Page):
    username = 'Raul'
    password = 'dguihsja'

    login_page = LoginPage(page)
    login_page.login(username, password)

    expect(login_page.login_status).to_have_text('Invalid username/password')