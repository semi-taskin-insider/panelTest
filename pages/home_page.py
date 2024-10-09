import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage
class HomePage(BasePage):
    """
    Performs transactions on the Home Page
    """
    EXPERIENCE_BTN = (By.XPATH, ".//li[contains(@class,'in-sidebar-wrapper__groups')]")
    OPTIMIZE_DROPDOWN = (By.XPATH, ".//*[text()='Optimize']")
    INSTORY_BTN = (By.CSS_SELECTOR, "a[href='/instory-all']")

    def clicking_instory(self, index):
        """
        goes instory campaigns page
        """
        self.click_index_element(index, *self.EXPERIENCE_BTN)
        time.sleep(1)
        self.click_element(*self.OPTIMIZE_DROPDOWN)
        time.sleep(1)
        self.click_element(*self.INSTORY_BTN)
        time.sleep(1)
