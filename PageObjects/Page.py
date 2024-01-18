import testData.common as common
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.url = common.URL

    def init_site(self):
        """ Initialize the URL. """
        self.driver.get(self.url)

    def click_element(self, locator, wait_time=3):
        element = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(locator)
        )
        element.click()

    def select_option_by_text(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)
