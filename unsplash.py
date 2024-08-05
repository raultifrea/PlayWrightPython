from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # Create a new page
    page = browser.new_page()
    # Visit Playwright website
    url = 'https://unsplash.com'
    page.goto(url)

    page.get_by_alt_text("A man sitting at a table with a laptop and cell phone").highlight()
    page.get_by_alt_text("A man standing on top of an airplane at night").click()

    browser.close()