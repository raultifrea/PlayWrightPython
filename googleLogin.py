from playwright.sync_api import sync_playwright
import json, time

json_file_path = 'credentials.json'
with open(json_file_path, 'r') as file:
    data = json.load(file)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.set_viewport_size({"width":922, "height":950})
    page.goto('https://accounts.google.com')
    email_input = page.get_by_label("Email or phone")
    email_input.fill(data['email'])
    next_btn = page.get_by_role('button', name='Next')
    next_btn.click()
    password_input = page.locator('input[name="Passwd"]')
    password_input.fill(data['password'])
    next_btn.click()
    time.sleep(5)
    browser.close()

