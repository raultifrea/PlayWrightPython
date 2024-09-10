from playwright.sync_api import sync_playwright

def on_load(page):
    print("Page loaded:", page)

def on_request(request):
    print("Request sent", request)

def on_filechooser(file_chooser):
    print("File chooser opened", file_chooser)
    file_chooser.set_files("file.txt")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    page.on('load', on_load) #prints the document
    # page.on('request', on_request)  #prints all requests
    # page.on("filechooser", on_filechooser)

    page.goto('https://bootswatch.com/default')

    # file_input = page.locator('#formFile')
    # file_input.click()

    browser.close()

def on_dialog(dialog):
    print('dialog opened')
    dialog.accept("Inputing something")
    # dialog.dismiss()
    
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True, slow_mo=1000)
    page = browser.new_page()

    page.goto('https://testpages.eviltester.com/styled/alerts/alert-test.html')

    page.on('dialog', on_dialog)

    alert_btn = page.get_by_text('Show alert box')
    alert_btn.click()

    confirm_btn = page.get_by_text('Show confirm box')
    confirm_btn.click()

    prompt_btn = page.get_by_text('Show prompt box')
    prompt_btn.click()

    browser.close()