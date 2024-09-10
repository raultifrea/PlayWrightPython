from playwright.sync_api import Page, expect
import re

#Execute via CLI using pytest -v page_assertions.py

DOCS_URL = 'https://playwright.dev/python/docs/intro'

def test_playwright_dev_page(page: Page):
    page.goto("https://playwright.dev/python/")

    #assert inner text
    heading = page.locator('h1.hero__title')
    expect(heading).to_contain_text('testing')
    #exact match
    expect(heading).to_have_text('Playwright enables reliable end-to-end testing for modern web apps.') 

    dropdown_menu = page.locator('ul.dropdown__menu')
    expect(dropdown_menu).to_contain_text("Java")
    expect(dropdown_menu).to_contain_text("Node.js")
    expect(dropdown_menu).to_contain_text(".NET")
    expect(dropdown_menu).to_contain_text("Python")

    docs_link = page.get_by_role('link', name='Docs')
    #exact match required
    expect(docs_link).to_have_class("navbar__item navbar__link")
    #partial match using RegEx
    expect(docs_link).to_have_class(re.compile(r"navbar__link"))
    expect(docs_link).to_have_class(re.compile(r"^navbar__item"))
    #exact match required
    expect(docs_link).to_have_attribute('href', '/python/docs/intro')

    input = page.get_by_placeholder("Search docs")
    expect(input).to_be_hidden()
    search_btn = page.locator('.DocSearch-Button-Container')
    search_btn.press("Control+KeyK") #same as search_btn.click()
    expect(input).to_be_editable()
    expect(input).to_be_empty()

    query = 'assertions'
    input.fill(query)
    expect(input).to_have_value(query)
    page.keyboard.press("Escape")

    link = page.get_by_role('link', name='GET STARTED')
    expect(link).to_be_visible()
    expect(link).to_be_enabled()
    link.click()

    #non-existent element
    link2 = page.get_by_role('link', name='I do not exist')
    expect(link2).not_to_be_visible()
    #same as
    expect(link2).to_be_hidden()

    assert page.url == DOCS_URL
    #same as
    expect(page).to_have_url(DOCS_URL)
    expect(page).to_have_title('Installation | Playwright Python')

def test_bootswatch_page(page: Page):
    page.goto('https://bootswatch.com/default/')

    checked_checkbox = page.get_by_label('Checked checkbox')
    default_checkbox = page.get_by_label('Default checkbox')

    expect(checked_checkbox).to_be_checked()
    expect(default_checkbox).not_to_be_checked()

    option_menu = page.get_by_label('Example select')
    expect(option_menu).to_have_value('1')

    multi_option_menu = page.get_by_label('Example multiple select')
    expect(multi_option_menu).to_have_values([]) #none selected
    multi_option_menu.select_option(["2", "4"])
    expect(multi_option_menu).to_have_values(["2", "4"])