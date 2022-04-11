import pytest
from playwright.sync_api import Playwright


@pytest.mark.integ
def test_login(login_set_up) -> None:
    page = login_set_up
    # page.wait_for_timeout(1000)
    #
    # page.locator("text=Log in").click()
    #
    # page.locator("[data-testid=\"signUp\\.switchToSignUp\"]").click()
    # page.locator("[data-testid=\"switchToEmailLink\"] [data-testid=\"buttonElement\"]").click()
    # page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").click()
    # page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").fill("talgreen1@yahoo.com")
    # page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").press("Tab")
    # page.locator("input[type=\"password\"]").fill("123456")
    # page.locator("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]").click()

    assert page.is_visible("[aria-label=\"Cart with 0 items\"]")
