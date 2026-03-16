from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.employee_page import EmployeePage


def test_search_existing_employee(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Admin", "admin123")

    DashboardPage(driver).go_to_pim()

    emp = EmployeePage(driver)
    emp.search_employee("Admin")

    assert emp.get_result_count() > 0


def test_search_nonexistent_employee(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Admin", "admin123")

    DashboardPage(driver).go_to_pim()

    emp = EmployeePage(driver)
    emp.search_employee("xyzxyzxyz123")

    assert emp.no_records_found()