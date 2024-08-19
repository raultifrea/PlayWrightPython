from playwright.sync_api import sync_playwright

#storage_path = 'playwright/.auth/storage_state.json'
storage_path = '/root/PlayWrightPython/playwright/.auth/storage_state.json'

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    context = browser.new_context(storage_state=storage_path)
    page = context.new_page()
    page.goto('https://gmail.com')

    new_emails = []
    
    emails = page.locator('div.UI table tr') # all email entries
    
    for email in emails.all():
        if email.locator("td li[data-tooltip='Mark as read']").count() == 1:
            sender_name = email.locator('td span[email]:visible').inner_text()
            email_title = email.locator('td span[data-thread-id]:visible').inner_text()
            new_emails.append([sender_name, email_title])
    
    if len(new_emails) == 0:
        print("No new emails !")
    else:
        print(f"{len(new_emails)} new emails!")
        print('-'*30)

        for index, new_email in enumerate(new_emails):
            print(f'Sender: {new_email[0]}')
            print(f'Subject: {new_email[1]}')
            print('-'*30)
    
    context.close()
