import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage
class LaunchPage(BasePage):
    """
    Performs transactions on the Launch Page
    """
    LANGUAGE_DROPDOWN = (By.ID, "personalization-language")
    ALL_LANGUAGES = (By.XPATH, ".//a[contains(@class,'all-languages')]")
    DATE_DROPDOWN = (By.CSS_SELECTOR, ".form-control.reportrange-text")
    CHOOSING_DATE_BTN = (By.CLASS_NAME, "weekend")
    TIME_DROPDOWN = (By.CSS_SELECTOR, "input[name='endHour']")
    CHOOSING_TIME_BTN = (By.CSS_SELECTOR, "p.option__2")
    DISPLAY_TIME_DROPDOWN_BTN = (By.XPATH, ".//div[contains(@class,'qa-accordion-toggle')]")
    DISPLAY_DAYS = (By.CSS_SELECTOR, ".d-i-b.in-radio-button-wrapper__label")
    ACTIVE_ON_SATURDAY = (By.CSS_SELECTOR, "label[for='Saturday']")
    ACTIVE_ON_SUNDAY = (By.CSS_SELECTOR, "label[for='Sunday']")
    ACTIVE_ON_MONDAY = (By.CSS_SELECTOR, "label[for='Monday']")
    ACTIVE_ON_TUESDAY = (By.CSS_SELECTOR, "label[for='Tuesday']")
    ADVANCED_DROPDOWN_BTN = (By.XPATH, ".//div[contains(@class,'qa-accordion-toggle')]")
    PRIORITY_DROPDOWN = (By.ID, "priority")
    PRIORITY_BTN = (By.CSS_SELECTOR, ".option__2.priority-2")
    NOTE_FIELD = (By.ID, "note")
    note = "semitest"
    TEST_BTN = (By.CSS_SELECTOR, "label[for='Test']")
    SAVE_AND_NEXT_BTN = (By.ID, "save-and-next")

    def choosing_language(self):
        """
        changes language of the campaign
        """
        time.sleep(2)
        self.click_element(*self.LANGUAGE_DROPDOWN)
        time.sleep(0.5)
        self.click_element(*self.ALL_LANGUAGES)

    def changing_date(self, index, weekend):
        """
        changes create dates of the campaign
        """
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        self.click_index_element(index, *self.DATE_DROPDOWN)
        time.sleep(1)
        self.click_index_element(weekend, *self.CHOOSING_DATE_BTN)

    def changing_end_time(self, index):
        """
        changes end time of the campaign
        """
        self.click_element(*self.TIME_DROPDOWN)
        time.sleep(0.5)
        self.click_index_element(index, *self.CHOOSING_TIME_BTN)

    def changing_display_time(self, index, days):
        """
        changes display time of the campaign
        """
        self.click_index_element(index, *self.DISPLAY_TIME_DROPDOWN_BTN)
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(2)
        self.click_index_element(days, *self.DISPLAY_DAYS)
        time.sleep(0.5)
        self.click_element(*self.ACTIVE_ON_SATURDAY)
        self.click_element(*self.ACTIVE_ON_SUNDAY)
        self.click_element(*self.ACTIVE_ON_MONDAY)
        self.click_element(*self.ACTIVE_ON_TUESDAY)

    def changing_priority(self, index):
        """
        changes priority of the campaign
        """
        self.driver.execute_script("window.scrollTo(0, 1650)")
        time.sleep(1)
        self.click_index_element(index, *self.ADVANCED_DROPDOWN_BTN)
        time.sleep(0.5)
        self.click_element(*self.PRIORITY_DROPDOWN)
        time.sleep(1)
        self.click_element(*self.PRIORITY_BTN)

    def filling_notes(self):
        """
        fills notes step
        """
        self.driver.execute_script("window.scrollTo(0, 2000)")
        time.sleep(1)
        self.send_text(self.note, *self.NOTE_FIELD)

    def making_status_test(self):
        """
        makes campaign status test
        """
        self.click_element(*self.TEST_BTN)

    def clicking_save_and_next_btn(self):
        """
        click save button and launch campaign
        """
        self.click_element(*self.SAVE_AND_NEXT_BTN)
        time.sleep(2)
