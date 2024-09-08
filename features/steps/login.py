from behave import *
from playwright.sync_api import expect

@given('username and pwd password')
def fill_username_and_password(context):
    context.page.goto('http://uitestingplayground.com/sampleapp')
    context.page.get_by_placeholder('User Name').fill('name')
    context.page.get_by_placeholder('********').fill('pwd')

@when('login in button clicked')
def click_login(context):
    context.page.locator('#login').click()

@then('show welcome message')
def expect_welcome_message(context):
    expect(context.page.locator('label#loginstatus')).to_have_text(f'Welcome, name!')