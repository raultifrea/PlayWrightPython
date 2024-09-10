from playwright.sync_api import sync_playwright
from time import perf_counter


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    page = browser.new_page()
    url = 'https://www.scrapethissite.com/pages/ajax-javascript/'
    page.goto(url)

    link = page.get_by_role('link', name='2015')
    link.click()

    print("Loading oscars for 2015")
    start = perf_counter()
    first_table_data = page.locator('td.film-title').first
    first_table_data.wait_for()

    time_taken = perf_counter() - start
    print(f"...oscars are loaded in {round(time_taken, 2)}s")

    browser.close()