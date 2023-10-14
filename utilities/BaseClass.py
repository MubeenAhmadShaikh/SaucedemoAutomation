import inspect
import logging
import colorama
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest


from pageObjects.LoginPage import LoginPage


@pytest.mark.usefixtures("setup")
class BaseClass:

    @pytest.fixture(scope="module")
    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        # Following code for color logging which is applied only in console and not in log files
        # ch = logging.StreamHandler()
        # ch.setLevel(logging.DEBUG)
        # ch.setFormatter(CustomFormatter())
        # logger.addHandler(ch)

        fh = logging.FileHandler("../logs/logging.log")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(logging.Formatter("%(asctime)s - [%(module)s] - [%(filename)s:%(lineno)d] - [%(funcName)s - [%(levelname)s] - %(message)s"))
        logger.addHandler(fh)
        return logger

    def perform_complete_login(self):
        login_page = LoginPage(self.driver)
        # log.info("username name entered is " + getUserCreds['username'])
        login_page.getUserNameField().send_keys('standard_user')
        # log.info("password entered is " + getUserCreds['password'])
        login_page.getPasswordField().send_keys('secret_sauce')
        login_page.getLoginButton().click()

    def captureScreenShot(self, file_name):
        self.driver.get_screenshot_as_file(file_name)

    def selectOptionByText(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


