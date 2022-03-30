from playwright.sync_api import Playwright, sync_playwright

from pom.home_page_elements import HomePage


def test_main_page(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(30000)
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    assert page.is_visible(HomePage.celebrating_beauty_body)
    assert page.is_visible(HomePage.celebrating_beauty_header)


with sync_playwright() as playwright:
    test_main_page(playwright)
