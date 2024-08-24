from playwright.sync_api import Page, expect, TimeoutError
import pytest

def test_dynamic_id(page: Page):
    page.goto('http://uitestingplayground.com/dynamicid')

    button = page.get_by_role('button', name='Button with Dynamic ID')
    expect(button).to_be_visible()
    button.click()

def test_class_attribute(page: Page):
    page.goto('http://uitestingplayground.com/classattr')

    primary_btn = page.locator('button.btn-primary')
    #same but using xpath selector
    # primary_btn = page.locator('//button[contains(@class, "btn-primary")]')
    expect(primary_btn).to_be_visible()
    primary_btn.click()

def test_hidden_layers(page: Page):
    page.goto('http://uitestingplayground.com/hiddenlayers')

    green_btn = page.locator('#greenButton')
    green_btn.click()
    #make sure the button is not clickable twice
    with pytest.raises(TimeoutError):
        green_btn.click(timeout=2000)

def test_load_delay(page: Page):
    page.goto('http://uitestingplayground.com')

    delay_btn = page.get_by_role('link', name='Load Delay')
    delay_btn.click()
    other_page_btn = page.get_by_role('button', name='Button Appearing After Delay')
    other_page_btn.wait_for(timeout=10_000)
    expect(other_page_btn).to_be_visible()

def test_ajax_data(page: Page):
    page.goto('http://uitestingplayground.com/ajax')

    btn_trigger = page.locator('#ajaxButton')
    btn_trigger.click()
    data = page.locator('p.bg-success')
    data.wait_for() #default 30 sec
    expect(data).to_be_visible()

def test_click(page: Page):
    page.goto('http://uitestingplayground.com/click')

    btn = page.locator('#badButton')
    btn.click()
    expect(btn).to_have_class('btn btn-success')

def test_text_input(page: Page):
    page.goto('http://uitestingplayground.com/textinput')

    query = 'Rapid'

    input = page.get_by_label('Set New Button Name')
    input.fill(query)

    btn = page.locator('#updatingButton')
    btn.click()
    expect(btn).to_have_text(query)

def test_text_input(page: Page):
    page.goto('http://uitestingplayground.com/scrollbars')

    btn = page.locator('#hidingButton')
    btn.scroll_into_view_if_needed()
    page.screenshot(path='test-scrollbars.jpg')


    
