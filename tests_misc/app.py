from playwright.sync_api import sync_playwright
from time import perf_counter

with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    # Create a new page
    page = browser.new_page()
    print("Page loading...")
    start = perf_counter()

    page.goto('https://bootswatch.com/default', wait_until='networkidle')
    #networkidle waits for all network requests to be sent/received - 1.9s
    #load waits for all resources to load -  1.5s
    #domcontentloaded does not wait for the resources to load -  1.03s
    #commit waits for playwright to find the html server response - 0.93s

    time_taken = perf_counter() - start
    print(f"...Page is loaded in {round(time_taken, 2)}s")

    # page.locator('#themes').click()
    # entry = page.locator('a.dropdown-item').first
    # entry.click(force=True) #Forcing the click skips the default timeout or any other 'timeout=x'

    browser.close()