from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from pages.campaigns_page import CampaignsPage
from pages.design_page import DesignPage
from pages.home_page import HomePage
from pages.goals_page import GoalsPage
from pages.launch_page import LaunchPage
from pages.login_page import LoginPage
from pages.rules_page import RulesPage
from pages.segment_page import SegmentPage


class BaseTest():

    def __init__(self):
        options = Options()
        options.add_argument("--disable-infobars")
        options.add_argument("start-maximized")
        options.add_argument("--disable-extensions")

        self.driver = webdriver.Chrome(options=options)
        self.url = "https://seleniumautomation.inone.useinsider.com/"
        self.wait = WebDriverWait(self.driver, 15)

        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.campaigns_page = CampaignsPage(self.driver)
        self.rules_page = RulesPage(self.driver)
        self.segment_page = SegmentPage(self.driver)
        self.design_page = DesignPage(self.driver)
        self.goals_page = GoalsPage(self.driver)
        self.launch_page = LaunchPage(self.driver)

    def navigate_to_home_page(self):
        """
        driver settings made and website published
        """
        self.driver.maximize_window()
        self.driver.get(self.url)


if __name__ == '__main__':
    BaseTest().navigate_to_home_page()
