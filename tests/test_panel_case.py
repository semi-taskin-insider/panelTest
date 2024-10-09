import time
import unittest
from base_test import BaseTest


class TestPanel(unittest.TestCase, BaseTest):
    """
    TEST CASE
            1. Log in the panel, go to Web Instory
            2. Create Web Instory campaign
            3. Fill all steps till Launch step
            4. Change campaign's language, date&time, display settings, add priority, notes
            and launch campaign as Active.
            5. Go to do list and check campaign status is Active and added variation is present in Test link menu
            6. Open campaign's details and check all information that was filled during launch is present there
            7. Go to website with the test link of the campaign.
            8. Verify that campaign is visible (Storage and class existence control is enough)
    """
    def setUp(self):
        """
        set ups testCheckPanel constructor
        """
        BaseTest.__init__(self)

    def test_panel(self):
        """
        This part of the program performs tests steps for creating instory campaign
        """

        self.navigate_to_home_page()
        self.login_page.writing_email()
        self.login_page.writing_password()
        self.login_page.clicking_login_button()
        time.sleep(1)

        self.home_page.clicking_instory(2)

        self.campaigns_page.clicking_create_btn()
        time.sleep(2)
        self.campaigns_page.writing_campaign_name()
        self.campaigns_page.clicking_campaign_create_btn()

        self.segment_page.clicking_save_and_next_btn()

        self.rules_page.choosing_page_type(0)
        self.rules_page.clicking_save_and_next_btn()

        self.design_page.adding_new_variant()
        self.design_page.appending_template()
        self.design_page.saving_template()
        self.design_page.clicking_save_and_next_btn()

        self.goals_page.clicking_save_and_next_btn()

        self.launch_page.choosing_language()
        self.launch_page.changing_date(1, 8)
        self.launch_page.changing_end_time(1)
        self.launch_page.changing_display_time(0, 3)
        self.launch_page.changing_priority(1)
        self.launch_page.filling_notes()
        self.launch_page.making_status_test()
        self.launch_page.clicking_save_and_next_btn()

        status_text = self.campaigns_page.getting_status()
        self.assertEqual("Test", status_text, "Status text is not equal")
        self.campaigns_page.clicking_test_menu(0)
        text_link_visibility = self.campaigns_page.checking_test_link_visibility()
        self.assertTrue(text_link_visibility, "Variation is not visible")
        self.campaigns_page.clicking_details_btn(0)
        priority_check = self.campaigns_page.checking_priority()
        self.assertEqual("2", priority_check, "Priority is not equal")
        note_check = self.campaigns_page.checking_note()
        self.assertEqual("test", note_check, "Notes are not equal")
        self.campaigns_page.closing_details(5)

    def tear_down(self):
        self.driver.quit()
