from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
class BasePage(object):

    def __init__(self, driver):
        """
        constructor with initial values
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    class SwitchFrame:
        """
        iFrame switch class
        """
        def __init__(self, driver, element):
            """
            constructor with initial values
            """
            self.driver = driver
            self.element = element

        def __enter__(self):
            """
            allows you to implement objects which can be used easily with the with statement.
            """
            self.driver.switch_to.frame(self.element)

        def __exit__(self, type, value, traceback):
            """
            allows you to implement objects which can be used easily with the with statement.
            """
            self.driver.switch_to.parent_frame()

    def find_element(self, *locator):
        """
        find element function
        """
        return self.driver.find_element(*locator)

    def click_index_element(self, index, *element):
        """
        finds index elements function
        """
        self.driver.click_index_element(*element)[index].click()

    def click_element(self, *locator):
        """
        performs the click function
        """
        self.find_element(*locator).click()

    def send_text(self, text, *locator):
        """
        performs the sending text function
        """
        self.find_element(*locator).send_keys(text)

    def clear_text(self, *locator):
        """
        performs the clear text function
        """
        self.find_element(*locator).clear()

        return self

    def hover(self, element="", *locator):
        """
        performs the hover function
        """
        if locator == "":
            element = self.find_element(*locator)
            ActionChains(self.driver).move_to_element(element).perform()
        else:
            ActionChains(self.driver).move_to_element(element).perform()
        return self

    def switch_frame(self, *locator):
        """
        performs the switching frame function
        """
        return self.SwitchFrame(self.driver, self.wait_for_element_visible(*locator))

    def wait_element(self, element):
        """
        allows the page to load and find the element
        """
        return self.wait.until(ec.presence_of_all_elements_located(element))

    def get_text(self, *element, index):
        """
        performs the getting text function
        """
        return self.wait.until(ec.presence_of_all_elements_located(*element))[index]

    def wait_for_element_clickable(self, *element):
        """
        allows the page to load until element is clickable
        """
        return self.wait.until(ec.element_to_be_clickable(*element))

    def wait_for_element_visible(self, *locator):
        """
        allows the page to load until element is visible
        """
        return self.wait.until(ec.visibility_of_element_located(*locator))

    def wait_for_element(self, *selector):
        """
        allows the page to load and find the element
        """
        return self.wait.until(ec.element_to_be_clickable(*selector))

    def click_elements(self, *selector, index):
        """
        performs the click function
        """
        self.wait_for_element(*selector)[index].click()
