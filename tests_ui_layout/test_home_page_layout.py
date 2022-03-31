from playwright.sync_api import Playwright

from pom.home_page_elements import HomePage


def test_about_us_section(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(30000)
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_timeout(1000)

    assert page.is_visible(HomePage.celebrating_beauty_body)
    assert page.is_visible(HomePage.celebrating_beauty_header)
