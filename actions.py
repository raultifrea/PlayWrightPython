from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    url = 'https://bootswatch.com/default'
    page.goto(url)

    button = page.get_by_role('button', name='Block button').first
    button.click()
    button.dblclick(delay=500) #optinal argument to delay the double click
    button.click(button="right") #right mouse button click
    button.click(modifiers=["Shift"]) #keep another button pressed while clicking e.g Ctrl/Alt

    outline_button = page.locator("button.btn-outline-primary")
    outline_button.hover() #take that Cypress

    input = page.get_by_placeholder('Enter email')
    input.fill("me@that.site") #same as .type()
    input.clear()
    input.type('me@that.site', delay=200)

    valid_input= page.locator('#inputValid')
    print(valid_input.input_value()) #correct value

    #Radio Buttons
    radio_option1 = page.locator('#optionsRadios1')
    radio_option2 = page.locator('#optionsRadios2')
    radio_option2.check()
    radio_option1.check()

    #Checkboxes
    checkbox = page.locator('#flexCheckDefault')
    checkbox.check() #same as click()
    print(checkbox.is_checked()) #prints True
    checkbox.uncheck()
    print(checkbox.is_checked()) #prints False
    checkbox.set_checked(True)
    print(checkbox.is_checked()) #prints True
    checkbox.set_checked(False)
    print(checkbox.is_checked()) #prints False

    #Switches
    switch = page.locator('#flexSwitchCheckDefault')
    switch.check()
    switch.uncheck()

    # DropDowns
    select = page.get_by_label('Example select')
    select.select_option("4")
    select.select_option("2")

    multi_select = page.get_by_label('Example multiple select')
    multi_select.select_option(["2", "4"])
    multi_select.select_option(["1", "3", "5"])

    dropdown = page.locator('button#btnGroupDrop1')
    dropdown.click()
    dropdown_link = page.locator('div.dropdown-menu:visible a:text("Dropdown link")').last #only the visible dropdown menu
    dropdown_link.click()

    #Upload File
    file_input = page.locator('#formFile')
    file_input.set_input_files("file.txt") #set_input_files(["multiple", "files"])

    with page.expect_file_chooser() as fc_info:
        file_input.click() #triggered the code that shows the file chooser
    
    file_chooser = fc_info.value #extracted the file chooser
    # file_chooser.set_files("app.py") #set the new files

    #Keyboard shortcurts
    textarea = page.get_by_label('Example textarea')
    textarea.fill("word")
    textarea.clear()

    textarea.press("KeyW")
    textarea.press("KeyO")
    textarea.press("KeyR")
    textarea.press("Shift+KeyD")
    textarea.press("Control+ArrowLeft")
    textarea.press("ArrowRight")






