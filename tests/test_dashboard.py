from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_dashboard_heading(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    heading = dashboard.get_page_heading()
    assert heading == "Dashboard"


def test_logout(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Admin", "admin123")

    from selenium.webdriver.support.ui import WebDriverWait
    WebDriverWait(driver, 15).until(
        lambda d: "dashboard" in d.current_url.lower()
    )

    dashboard = DashboardPage(driver)
    dashboard.logout()

    WebDriverWait(driver, 15).until(
        lambda d: "login" in d.current_url.lower()
    )
    assert "login" in driver.current_url.lower()