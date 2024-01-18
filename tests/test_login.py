import time

import pytest
from selenium.common.exceptions import NoSuchElementException
from testData.UserCredentials import UserCreds
import testData.common as common
from PageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestLoginPage(BaseClass):
    """ This class contains all the tests for login related scenarios. """

    def test_login_from_existing_data(self, get_user_credentials, get_logger):
        """Test logging in with a valid username and password."""
        log = get_logger
        log.info("Test Case Summary: Verify user is able to login to saucedemo website using valid credentials "
                 "and Unable to login using Invalid credentials.")
        log.info("Step 1: Launch the website https://www.saucedemo.com")
        log.info("Launching the browser and navigated to https://www.saucedemo.com")
        login_page = LoginPage(self.driver)
        # self.driver.implicitly_wait(4)
        log.info("Step 2: Enter the username")
        login_page.enter_username(get_user_credentials['username'])
        log.info("Username entered is : "+get_user_credentials['username'])
        log.info("Step 3: Enter the password")
        login_page.enter_password(get_user_credentials['password'])
        log.info("Password entered is : "+get_user_credentials['password'])
        log.info("Step 4: Click on login button")
        login_page.click_login()
        log.info("Clicked on Login button")
        log.info("Step 5: Verify user navigated to home page of Products and 'Products' title is displayed")
        try:
            assert login_page.title_exists()
            log.info("Products title exist, Login verification successful")
        except NoSuchElementException:
            try:
                assert login_page.error_message_exist()
                log.info(login_page.get_error_message_text())
            except NoSuchElementException:
                log.error("Error message not displayed for invalid credentials")
                pytest.fail("Error message for invalid credentials should be displayed")
        log.info("Closing the browser")

    @pytest.mark.negative
    def test_login_invalid_credentials(self, get_invalid_credentials, get_logger):
        """Test logging in with invalid username and password.
        Scenarios:
        1. Invalid username correct password
        2. Correct username invalid password
        3. Both username and password invalid
        4. Empty strings
        """
        login_page = LoginPage(self.driver)
        log = get_logger
        log.info("Test the login functionality with negative testing using multiple wrong credentials.")
        log.info("Step 1: Launch the website https://www.saucedemo.com")
        log.info("Launching the browser and navigated to https://www.saucedemo.com")
        log.info("Step 2: Enter the username")
        login_page.enter_username(get_invalid_credentials["username"])
        log.info("Username entered is: "+get_invalid_credentials["username"])
        log.info("Step 3: Enter Password")
        login_page.enter_password(get_invalid_credentials["password"])
        log.info("Password entered is: "+get_invalid_credentials["password"])
        log.info("Step 4: Click on Login button")
        login_page.click_login()
        try:
            assert login_page.error_message_exist()
            log.info("Verify user is unable to login and error message displayed is " +
                     login_page.get_error_message_text())
            log.info(login_page.get_error_message_text())
        except NoSuchElementException:
            log.error("Invalid login credentials and error message also not displayed")
            pytest.fail("Error message also not displayed for invalid credentials")
        log.info("Closing the browser")

    @pytest.mark.positive
    def test_login_standard_user(self, get_logger):
        """Test logging in with a valid standard user"""
        log = get_logger
        login_page = LoginPage(self.driver)
        log.info("Verify user is able to login successfully with standard user.")
        log.info("Step 1: Launch the website https://www.saucedemo.com")
        log.info("Launching the browser and navigated to https://www.saucedemo.com")
        log.info("Step 2: Enter the username")
        login_page.enter_username(common.STANDARD_USER)
        log.info("Username entered is: "+common.STANDARD_USER)
        log.info("Step 3: Enter Password")
        login_page.enter_password(common.STANDARD_PASSWORD)
        log.info("Password entered is: "+common.STANDARD_PASSWORD)
        log.info("Step 4: Click on login button")
        login_page.click_login()
        log.info("Verify user is successfully able to login and redirected to home page"
                 " with 'Products' title displayed")
        try:
            assert login_page.title_exists()
            log.info("User successfully logged in and Products title is displayed")
        except NoSuchElementException:
            log.error("'Products' title is not displayed or user is not redirected to home page")
            pytest.fail("'Products' title not displayed or user is not redirected to home page")
        log.info("Closing the browser")

    def test_login_problem_user(self, get_logger):
        """Test logging in with a valid problem user"""
        log = get_logger
        login_page = LoginPage(self.driver)
        log.info("Verify user is able to login successfully with problem user and no issues observed in login.")
        log.info("Step 1: Launch the website https://www.saucedemo.com")
        log.info("Launching the browser and navigated to https://www.saucedemo.com")
        log.info("Step 2: Enter the username")
        login_page.enter_username(common.PROBLEM_USER)
        log.info("Username entered is: " + common.PROBLEM_USER)
        log.info("Step 3: Enter Password")
        login_page.enter_password(common.STANDARD_PASSWORD)
        log.info("Password entered is: " + common.STANDARD_PASSWORD)
        log.info("Step 4: Click on login button")
        login_page.click_login()
        log.info(
            "Verify user is successfully able to login and redirected to home page with 'Products' title displayed")
        try:
            assert login_page.title_exists()
            log.info("User successfully logged in and Products title is displayed")
        except NoSuchElementException:
            log.error("'Products title is not displayed or user is not redirected to home page'")
            pytest.fail("'Products' title is not displayed or user is not redirected to home page")
        log.info("Closing the browser")

    @pytest.mark.negative
    def test_login_locked_out_user(self, get_logger):
        """Test logging in with a valid locked out user"""

        log = get_logger
        login_page = LoginPage(self.driver)
        log.info("Verify user is unable to login using the locked out user credentials.")
        log.info("Step 1: Launch the website https://www.saucedemo.com")
        log.info("Launching the browser and navigated to https://www.saucedemo.com")
        log.info("Step 2: Enter the username")
        login_page.enter_username(common.LOCKED_OUT_USER)
        log.info("Username entered is: " + common.LOCKED_OUT_USER)
        log.info("Step 3: Enter Password")
        login_page.enter_password(common.STANDARD_PASSWORD)
        log.info("Password entered is: " + common.STANDARD_PASSWORD)
        log.info("Step 4: Click on login button")
        login_page.click_login()
        log.info(
            "Verify user is unable to login using the locked out user credentials")
        try:
            assert login_page.error_message_exist()
            assert "locked out" in login_page.get_error_message_text()
            log.info("Error message is displayed as expected"+login_page.get_error_message_text())
        except NoSuchElementException:
            log.error("Error message for locked out user is not displayed")
            pytest.fail("Error message for locked out user is not displayed")
        log.info("Closing the browser")

    def test_login_performance_glitch_user(self, get_logger):
        """Test logging in with a valid performance glitch user"""
        login_page = LoginPage(self.driver)
        log = get_logger
        log.info("Verify user is able to login using performance glitch user.")
        log.info("Verify user is able to login using the performance glitch user credentials.")
        log.info("Step 1: Launch the website https://www.saucedemo.com")
        log.info("Launching the browser and navigated to https://www.saucedemo.com")
        log.info("Step 2: Enter the username")
        login_page.enter_username(common.GLITCH_USER)
        log.info("Username entered is: " + common.GLITCH_USER)
        log.info("Step 3: Enter the password")
        login_page.enter_password(common.STANDARD_PASSWORD)
        log.info("Password entered is: "+common.STANDARD_PASSWORD)
        log.info("Step 4: Click on login button")
        login_page.click_login()
        start_time = time.time()
        log.info("Verify there is a delay in login but user is able to login using performance glitch user credentials")
        try:
            end_time = time.time()
            delay = end_time - start_time
            assert login_page.title_exists()
            log.info("User is able to login successfully using performance glitch and 'Products' title also displayed "
                     "and the delay was of "+str(delay))
        except NoSuchElementException:
            log.error("'Products title is not displayed or user is not redirected to home page'")
            pytest.fail("'Products' title is not displayed or user is not redirected to home page")
        log.info("Closing the browser")

    # Fixtures
    @pytest.fixture(params=UserCreds.get_user_creds_data())
    def get_user_credentials(self, request):
        return request.param

    @pytest.fixture(params=UserCreds.get_invalid_user_credentials())
    def get_invalid_credentials(self, request):
        return request.param
