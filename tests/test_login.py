import pytest
from pages.login_page import LoginPage


def test_success_login(driver):
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url


def test_wrong_password(driver):
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")
    login_page.login("standard_user", "wrong_password")

    assert "Epic sadface" in login_page.get_error_text()


def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")
    login_page.login("locked_out_user", "secret_sauce")

    assert "locked out" in login_page.get_error_text()


def test_empty_fields(driver):
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")
    login_page.login("", "")

    assert "Epic sadface" in login_page.get_error_text()


def test_performance_glitch_user(driver):
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")
    login_page.login("performance_glitch_user", "secret_sauce")

    assert "inventory.html" in driver.current_url