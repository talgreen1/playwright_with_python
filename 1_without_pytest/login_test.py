#To open code gen: playwright codegen https://symonstorozhenko.wixsite.com/website-1

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
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

    assert page.is_visible("[aria-label=\"Cart with 0 items\"]")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
