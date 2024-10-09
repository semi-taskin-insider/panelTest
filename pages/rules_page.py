import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage
class RulesPage(BasePage):
    """
    Performs transactions on the Rules Page
    """

    RULE_BTN = (By.XPATH, ".//div[contains(@class,'clearfix mb-2')]")
    CONDITION_LIST = (By.ID, "conditionList0")
    PAGE_TYPE = (By.XPATH, ".//a[contains(@class,'page-type')]")
    SAVE_AND_NEXT_BTN = (By.ID, "save-and-next")

    def choosing_page_type(self, index):
        """
        adds page type rule
        """
        self.click_index_element(index, *self.RULE_BTN)
        time.sleep(1)
        self.click_element(*self.CONDITION_LIST)
        time.sleep(1)
        self.click_element(*self.PAGE_TYPE)
        time.sleep(1)

    def clicking_save_and_next_btn(self):
        """
        saves rule step and goes next step
        """
        self.click_element(*self.SAVE_AND_NEXT_BTN)
        time.sleep(2)
