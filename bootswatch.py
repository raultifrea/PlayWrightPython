from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # Create a new page
    page = browser.new_page()
    # Visit Playwright website
    url = 'https://bootswatch.com/default'
    page.goto(url)

    btn = page.get_by_role('button', name='Default button')
    btn.highlight()
    btn.click()

    heading = page.get_by_role('heading', name='Heading 2')
    heading.highlight()

    checkbox = page.get_by_role('checkbox', name='Default checkbox')
    checkbox.highlight()

    email_input = page.get_by_label('Email address')
    email_input.highlight()

    password = page.get_by_label('Password')
    password.highlight()

    page.get_by_label('Example textarea').highlight()
    page.get_by_placeholder("Enter email").highlight()
    page.get_by_placeholder("Password").highlight()
    page.get_by_text('with faded secondary text').highlight()
    page.get_by_text('Small button').highlight()
    page.get_by_text('Middle').highlight()

    page.get_by_text('fine print.').highlight()
    #same thing as False is implicit
    page.get_by_text('fine print.', exact=False).highlight()
    #only if this is the exact text
    page.get_by_text('fine print.', exact=True).highlight()

    #same outcome as 'attr' is the only text in the element
    page.get_by_text('attr', exact=True).highlight()
    page.get_by_text('attr', exact=False).highlight()

    page.get_by_title("Source Title").highlight()

    #CSS selectors 
    page.locator("css=h1").highlight() # same as "h1" css= is implicitly selected in Playwright
    page.locator("footer").highlight()

    page.locator("button.btn-outline-success").highlight() #select by tag and class name
    page.locator("button.btn-outline-success").click()

    page.locator("button#btnGroupDrop1").highlight()
    page.locator("button#btnGroupDrop1").click()
    
    page.locator('input[readonly]').highlight()
    page.locator('input[value="correct value"]').highlight()

    #Hierarchy locators
    page.locator('nav.bg-dark a.nav-link.active').highlight() #selects the Home element on the dark navBar
    page.locator('div.bs-component > ul.list-group').highlight()

    #CSS Selectors - Pseudo Classes
    page.locator("h1:text('Navbars')").highlight() #loose selector, contains text
    page.locator("h1:text-is('Navs')").highlight() #strict selector, exact text
    page.locator('div.dropdown-menu:visible').highlight() #only visible selectors
    page.locator(':nth-match(button.btn-primary, 5)').highlight() #only fifth element that matches the selector is matched
    page.locator(':nth-match(button:text("Primary"), 1)').highlight() #only first element matching the text is selected, similar to .first()

    #Xpath selectors - XML Query Language
    page.locator("xpath=//h1").highlight()
    page.locator("//h1[@id='navbars']").highlight()
    page.locator('//input[@readonly]').highlight()
    page.locator("//input[@value='wrong value']").highlight()
    page.locator("//h1[text()='Heading 1']").highlight()
    page.locator("//h1[contains(text(), 'Head')]").highlight()
    page.locator("//button[contains(@class, 'btn-outline-primary')]").highlight()
    page.locator("//input[contains(@value, 'correct')]").highlight()

    #Misc
    page.get_by_role('button', name="Primary").locator("nth=0").highlight() #selects the first matched locator using nth
    page.get_by_role('button', name="Primary").locator("nth=1").highlight() #selects the second matched locator using nth
    page.locator('button').locator('nth=18').highlight() #also selects the 19th matched locator using nth 

    page.get_by_label('Email address').locator('..').highlight() # get the parent element of the matched element
    page.locator('id=btnGroupDrop1').highlight() #same as #btnGroupDrop1
    page.locator('div.dropdown-menu').locator('visible=true').highlight() #only the visible ones are matched
    page.locator('div.dropdown-menu').locator('visible=false').highlight() #only the invisible ones are matched
    page.get_by_role('heading').filter(has_text='Heading').highlight() #filter h tags that contain Heading as text, only

    page.locator('label').filter(has=page.get_by_label('Password')).highlight()
    #same as
    page.locator('label').get_by_label('Password').highlight()

    browser.close()
