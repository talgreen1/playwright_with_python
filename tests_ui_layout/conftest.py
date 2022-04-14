import pytest


@pytest.fixture(scope="session")
def context_creation(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(30000)
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    page.wait_for_timeout(1000)

    page.locator("text=Log in").click()

    page.locator("[data-testid=\"signUp\\.switchToSignUp\"]").click()
    page.locator("[data-testid=\"switchToEmailLink\"] [data-testid=\"buttonElement\"]").click()
    page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").click()
    page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").fill("talgreen1@yahoo.com")
    page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").press("Tab")
    page.locator("input[type=\"password\"]").fill("123456")
    page.locator("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]").click()

    yield context

@pytest.fixture()
def login_set_up(context_creation):
    context = context_creation
    page = context.new_page()

    page.set_default_timeout(30000)
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    yield page
