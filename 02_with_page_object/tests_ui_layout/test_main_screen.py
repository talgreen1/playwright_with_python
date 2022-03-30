from playwright.sync_api import sync_playwright

from ..pom.home_page_elements import HomePage


def test_main_page(set_up) -> None:
    page = set_up

    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    assert page.is_visible(HomePage.celebrating_beauty_body)
    assert page.is_visible(HomePage.celebrating_beauty_header)


with sync_playwright() as playwright:
    test_main_page(playwright)
