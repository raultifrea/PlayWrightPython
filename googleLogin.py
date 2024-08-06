from playwright.sync_api import sync_playwright
import json

storage_path = 'playwright/.auth/storage_state.json'

json_file_path = 'credentials.json'
with open(json_file_path, 'r') as file:
    data = json.load(file)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000, args=["--disable-dev-shm-usage", "--disable-blink-features=AutomationControlled"],
    ignore_default_args=['--disable-component-extensions-with-background-pages'])

    context = browser.new_context(storage_state=storage_path)
    page = context.new_page()

    page.set_viewport_size({"width":922, "height":950})
    page.goto('https://accounts.google.com')

    #First time needed to login and create storage state
    # email_input = page.get_by_label("Email or phone")
    # email_input.fill(data['email'])

    # next_btn = page.get_by_role('button', name='Next')
    # next_btn.click()

    # password_input = page.locator('input[name="Passwd"]')
    # password_input.fill(data['password'])
    # next_btn.click()

    # save authentication context
    # context.storage_state(path=storage_path)

    context.close()

