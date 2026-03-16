from selenium.webdriver.common.by import By
from utils.base_page import BasePage


class EmployeePage(BasePage):

    EMPLOYEE_NAME_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']")
    SEARCH_BTN          = (By.XPATH, "//button[normalize-space()='Search']")
    RESULT_ROW          = (By.CSS_SELECTOR, ".oxd-table-body .oxd-table-row")
    NO_RECORDS_MSG      = (By.XPATH, "//span[text()='No Records Found']")

    def search_employee(self, name):
        self.type(self.EMPLOYEE_NAME_INPUT, name)
        self.click(self.SEARCH_BTN)

    def get_result_count(self):
        rows = self.driver.find_elements(*self.RESULT_ROW)
        return len(rows)

    def no_records_found(self):
        return self.is_visible(self.NO_RECORDS_MSG)