from playwright.sync_api import Page

class ContactUsPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://symonstorozhenko.wixsite.com/website-1/contact")

    def submit_form(self, name, address, email, phone, subject, message):
        self.page.locator("[placeholder=\"Enter your name\"]").fill(name)
        self.page.locator("[placeholder=\"Enter your address\"]").fill(address)
        self.page.locator("[placeholder=\"Enter your email\"]").fill(email)
        self.page.locator("[placeholder=\"Enter your phone number\"]").fill(phone)
        self.page.locator("[placeholder=\"Type the subject\"]").fill(subject)
        self.page.locator("textarea").fill(message)
        self.page.locator("[data-testid=\"buttonElement\"]").click()
