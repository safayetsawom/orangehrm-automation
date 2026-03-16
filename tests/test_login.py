from pages.login_page import LoginPage


def test_valid_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("Admin", "admin123")

    from selenium.webdriver.support.ui import WebDriverWait
    WebDriverWait(driver, 15).until(
        lambda d: "dashboard" in d.current_url.lower()
    )
    assert "dashboard" in driver.current_url.lower()

def test_invalid_login_wrong_password(driver):
    page = LoginPage(driver)
    page.open()
    page.login("Admin", "wrongpass")
    error = page.get_error_message()
    assert "Invalid credentials" in error


def test_empty_fields(driver):
    page = LoginPage(driver)
    page.open()
    page.login("", "")
    assert "login" in driver.current_url.lower()