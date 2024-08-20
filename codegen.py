from playwright.sync_api import Page

# run in CLI using playwright codegen playwright.dev (name of site)

def test_example(page: Page) -> None:
    page.goto("http://playwright.dev/")
    page.get_by_role("link", name="Get started").click()
    page.get_by_role("link", name="How to install Playwright").click()
    page.get_by_role("button", name="Node.js").click()
    page.get_by_role("link", name="Python").click()
    page.get_by_label("Search").click()
    page.get_by_placeholder("Search docs").click()
    page.get_by_placeholder("Search docs").fill("C#")
    page.get_by_placeholder("Search docs").press("Enter")
    page.get_by_role("link", name="Next CDPSession »").click()
