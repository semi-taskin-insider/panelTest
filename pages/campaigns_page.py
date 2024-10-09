import time
from base.base_page import BasePage
from selenium.webdriver.common.by import By
class CampaignsPage(BasePage):
    """
    Performs transactions on the Campaigns Pag
"""
    CREATE_BTN = (By.ID, "create-mobile-campaign")
    CAMPAIGN_NAME = (By.ID, "campaign-name")
    campaign_name = "semitest"
    CAMPAIGN_CREATE_BTN = (By.ID, "accept")
    STATUS_TEST = (By.CSS_SELECTOR, ".vuetable-slot.camp-status p")
    TEST_MENU_BTN = (By.XPATH, ".//p[text()= ' Test Link ']")  # 0'a tiklat
    VARIATION_BTN = (By.CSS_SELECTOR, ".in-box .clearfix")
    TEST_LINK_URL = (By.CSS_SELECTOR, ".in-box .clearfix a")
    OPTION_0_CHECK = (By.XPATH, ".//p[contains(@class,'option__0')]")
    DETAILS_BTN = (By.XPATH, ".//p[text()=' Details ']")  # 0'a tiklat
    PRIORITY_VALUE = (By.ID, "priority-value")
    NOTE_TEXT_VALUE = (By.XPATH, ".//p[contains(@class,'personalization-note')]")
    CLOSE_BTN = (By.CSS_SELECTOR, "svg[class='icon qa-icon name']")
    USER_DROPDOWN_BTN = (By.CSS_SELECTOR, "li:nth-child(6) > a")
    GENERATE_BTN = (By.LINK_TEXT, "Generate")

    def clicking_create_btn(self):
        """
        clicks create create button
        """
        self.click_element(*self.CREATE_BTN)

    def writing_campaign_name(self):
        """
        write campaign name
        """
        self.send_text(self.campaign_name, *self.CAMPAIGN_NAME)

    def clicking_campaign_create_btn(self):
        """
        clicks campaign create button
        """
        self.click_element(*self.CAMPAIGN_CREATE_BTN)
        time.sleep(2)

    def generating_campaign(self):
        """
        generates campaign
        """
        i = 0
        while i < 3:
            self.wait_for_element_clickable(self.USER_DROPDOWN_BTN).click()
            self.wait_for_element_clickable(self.GENERATE_BTN).click()
            time.sleep(14)
            i = i + 1

    def getting_status(self):
        """
        gets status of the campaign
        """
        time.sleep(2)
        return self.find_element(*self.STATUS_TEST).text

    def clicking_test_menu(self, index):
        """
        clicks test link menu
        """
        time.sleep(2)
        self.click_index_element(index, *self.TEST_MENU_BTN)

    def checking_test_link_visibility(self):
        """
        checks test link
        """
        time.sleep(2)
        return self.find_element(*self.OPTION_0_CHECK)

    def clicking_details_btn(self, index):
        """
        clicks details button
        """
        time.sleep(2)
        self.click_index_element(index, *self.DETAILS_BTN)

    def checking_priority(self):
        """
        checks priority of the campaign
        """
        time.sleep(2)
        return self.find_element(*self.PRIORITY_VALUE).text

    def checking_note(self):
        """
        checks notes of the campaign
        """
        time.sleep(2)
        return self.find_element(*self.NOTE_TEXT_VALUE).text

    def closing_details(self, index):
        """
        closes details
        """
        self.click_index_element(index, *self.CLOSE_BTN)

    def go_to_test_link(self):
        """
        goes test link
        """
        self.wait_for_element_clickable(self.VARIATION_BTN)
        self.hover(self.click_index_element(0, *self.VARIATION_BTN))
        self.driver.get(self.click_index_element(0, *self.TEST_LINK_URL).get_attribute('href'))
