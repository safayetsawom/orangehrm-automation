from selenium.webdriver.common.by import By
from utils.base_page import BasePage


class DashboardPage(BasePage):

    PAGE_HEADER    = (By.XPATH, "//h6[text()='Dashboard']")
    USER_DROPDOWN  = (By.CSS_SELECTOR, ".oxd-userdropdown-tab")
    LOGOUT_LINK    = (By.XPATH, "//a[text()='Logout']")
    PIM_MENU       = (By.XPATH, "//span[text()='PIM']")

    def get_page_heading(self):
        return self.get_text(self.PAGE_HEADER)

    def logout(self):
        self.click(self.USER_DROPDOWN)
        self.click(self.LOGOUT_LINK)

    def go_to_pim(self):
        self.click(self.PIM_MENU)