import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def set_up(page):
    page.set_default_timeout(30000)
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    yield page
