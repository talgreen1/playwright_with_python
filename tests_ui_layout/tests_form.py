from playwright.sync_api import Playwright, sync_playwright

from pom.contact_us_page import ContactUsPage
from pom.home_page_elements import HomePage

def submit_form_test(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    contact_us_page = ContactUsPage(page)
    page.set_default_timeout(30000)
    contact_us_page.navigate();
    contact_us_page.submit_form("tal", "add", "tal@gmail.com", "12325", "subj", "hello")
    # page.goto("https://symonstorozhenko.wixsite.com/website-1")



with sync_playwright() as playwright:
    submit_form_test(playwright)
