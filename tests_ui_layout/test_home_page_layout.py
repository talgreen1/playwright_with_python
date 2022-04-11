# import pytest
# from playwright.sync_api import Playwright
#
# from pom.home_page_elements import HomePage
#
#
# @pytest.mark.smoke
# def test_about_us_section(set_up) -> None:
#     page = set_up
#     page.wait_for_timeout(1000)
#
#     assert page.is_visible(HomePage.celebrating_beauty_body)
#     assert page.is_visible(HomePage.celebrating_beauty_header)
#
#
# def test_about_us_section_1(set_up) -> None:
#     page = set_up
#     page.wait_for_timeout(1000)
#
#     assert page.is_visible(HomePage.celebrating_beauty_body)
#     assert page.is_visible(HomePage.celebrating_beauty_header)
