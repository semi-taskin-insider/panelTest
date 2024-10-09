import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage


class SegmentPage(BasePage):
    """
    Performs transactions on the Segment Page
    """

    SAVE_AND_NEXT_BTN = (By.ID, "save-and-next")

    def clicking_save_and_next_btn(self):
        """
        saves segment step and goes next step
        """
        time.sleep(5)
        self.click_element(*self.SAVE_AND_NEXT_BTN)
        time.sleep(5)
