import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage
class GoalsPage(BasePage):
    """
    Performs transactions on the Goals Page
    """

    SAVE_AND_NEXT_BTN = (By.ID, "save-and-next")

    def clicking_save_and_next_btn(self):
        """
        saves goals step and goes next step
        """
        time.sleep(3)
        self.click_element(*self.SAVE_AND_NEXT_BTN)
        time.sleep(2)
