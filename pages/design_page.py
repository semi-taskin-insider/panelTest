import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage
class DesignPage(BasePage):
    """
    Performs transactions on the Design Page
    """

    ADD_NEW_VARIANT_BTN = (By.ID, "add-new-variation")
    SELECT_BTN = (By.CLASS_NAME, "btn-select")
    OK_BTN = (By.CLASS_NAME, "inline-select-notification-confirm")
    TOP_HEADER_BTN = (By.CLASS_NAME, 'top-header')
    IFRAME_BTN = (By.ID, 'iframe-edit')
    APPEND_AFTER_BTN = (By.CLASS_NAME, 'append-after')
    TEMPLATE_SAVE_BTN = (By.CLASS_NAME, 'btn-save')
    SAVE_AND_NEXT_BTN = (By.ID, "save-and-next")

    def adding_new_variant(self):
        """
        clicks new variant button and chooses template
        """
        time.sleep(4)
        self.click_element(*self.ADD_NEW_VARIANT_BTN)
        time.sleep(15)
        self.click_element(*self.SELECT_BTN)
        time.sleep(3)
        self.click_element(*self.OK_BTN)

    def appending_template(self):
        """
        appends template to the action builder
        """
        with self.switch_frame(self.IFRAME_BTN):
            self.wait_for_element_clickable(self.TOP_HEADER_BTN).click()
        self.wait_for_element_clickable(self.APPEND_AFTER_BTN).click()

    def saving_template(self):
        """
        saves templates
        """
        time.sleep(5)
        self.wait_for_element_clickable(self.TEMPLATE_SAVE_BTN).click()

    def clicking_save_and_next_btn(self):
        """
        saves design step and goes to next step
        """
        self.click_element(*self.SAVE_AND_NEXT_BTN)
        time.sleep(2)
