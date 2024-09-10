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

def test_scrollbars(page: Page):
    page.goto('http://uitestingplayground.com/scrollbars')

    btn = page.locator('#hidingButton')
    btn.scroll_into_view_if_needed()
    page.screenshot(path='test-scrollbars.jpg')

def test_dynamic_table(page: Page):
    page.goto('http://uitestingplayground.com/dynamictable')

    label = page.locator('p.bg-warning').inner_text()
    percentage = label.split()[-1]


    column_headers = page.get_by_role('columnheader')
    cpu_column = None
    for index in range(column_headers.count()):
        column_header = column_headers.nth(index)
        if column_header.inner_text() == 'CPU':
            cpu_column = index
            break
    assert cpu_column != None

    rowgroup = page.get_by_role('rowgroup').last
    chrome_row = rowgroup.get_by_role('row').filter(has_text="Chrome")
    chrome_cpu_value = chrome_row.get_by_role('cell').nth(cpu_column)

    expect(chrome_cpu_value).to_have_text(percentage)  

def test_verify_text(page: Page):
    page.goto('http://uitestingplayground.com/verifytext')

    parent = page.locator('div.bg-primary').get_by_text('Welcome') #partial match

    expect(parent).to_have_text("Welcome UserName!")

def test_progress_bar(page: Page):
    page.goto('http://uitestingplayground.com/progressbar')

    start_btn = page.locator('#startButton')
    stop_btn = page.locator('#stopButton')
    progressbar = page.locator('#progressBar')

    start_btn.click()
    while True:
        value_now = int(progressbar.get_attribute('aria-valuenow'))
        if value_now >= 75:
            break
        else:
            print(f'Percent: {value_now}%')
    stop_btn.click()

    assert value_now >= 75

def test_visibility(page: Page):
    page.goto('http://uitestingplayground.com/visibility')

    hide_btn = page.locator('#hideButton')
    opacity_btn = page.locator('#transparentButton')
    remove_btn = page.locator('#removedButton')
    invisible_btn = page.locator('#invisibleButton')
    zero_width_btn = page.locator('#zeroWidthButton')
    display_none_btn = page.locator('#notdisplayedButton')
    overlapped_btn = page.locator('#overlappedButton')
    offscreen_btn = page.locator('#offscreenButton')

    hide_btn.click()

    expect(remove_btn).to_be_hidden()
    expect(invisible_btn).to_be_hidden()
    expect(display_none_btn).to_be_hidden()

    with pytest.raises(TimeoutError):
        overlapped_btn.click(timeout=2000)
        
    expect(opacity_btn).to_have_css('opacity', '0')
    expect(zero_width_btn).to_have_css('width', '0px')

    expect(offscreen_btn).not_to_be_in_viewport()

@pytest.fixture()
def test_app_login(page: Page):
    page.goto('http://uitestingplayground.com/sampleapp')
    locators = {
        "username_input" : page.get_by_placeholder('User Name'),
        "password_input" : page.get_by_placeholder('********'),
        "login_btn" : page.locator('#login'),
        "login_status" : page.locator('label#loginstatus'),
    }
    return locators

def test_successful_login(test_app_login: Page):
    username = 'Raul'
    password = 'pwd'

    test_app_login['username_input'].fill(username)
    test_app_login['password_input'].fill(password)
    test_app_login['login_btn'].click()

    expect(test_app_login['login_status']).to_have_text(f'Welcome, {username}!')

def test_failed_login(test_app_login: Page):
    username = 'Raul'
    password = 'dguihsja'

    test_app_login['username_input'].fill(username)
    test_app_login['password_input'].fill(password)
    test_app_login['login_btn'].click()

    expect(test_app_login['login_status']).to_have_text('Invalid username/password')

def test_mouse_over(page: Page):
    page.goto('http://uitestingplayground.com/mouseover')

    link = page.get_by_title('Click me')
    link.hover()

    active_link = page.get_by_title('Active link')
    active_link.click(click_count=4)

    click_count = page.locator('span#clickCount')
    expect(click_count).to_have_text('4')

def test_nbsp(page: Page):
    page.goto('http://uitestingplayground.com/nbsp')

    #\u00a0 unicode character for nbsp
    page.locator("//button[text()='My\u00a0Button']").click(timeout=2000)

def test_overlapped(page: Page):
    page.goto('http://uitestingplayground.com/overlapped')

    input = page.get_by_placeholder('Name')
    div = input.locator('..') #parent selector
    div.hover()
    page.mouse.wheel(0, 200) #x, y
    data = 'Raul'
    input.fill(data)

    expect(input).to_have_value(data)





    
