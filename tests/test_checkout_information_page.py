import time

import pytest

from pageObjects.CartPage import CartPage
from pageObjects.ProductListPage import ProductsListPage
from utilities.BaseClass import BaseClass
from pageObjects.CheckoutFormPage import CheckoutFormPage
from selenium.common.exceptions import NoSuchElementException

class TestCheckoutInformationPage(BaseClass):

    def test_information_form(self, get_logger):
        """
        Scenarios:
        1. submit empty form and check error exist
        2. enter first_name only and submit form and check error exist
        3. enter last_name only and submit form and check err or exist
        4. enter post_code only and submit form and check error exist
        5. fill the complete form and submit
        :return: None
        """
        log = get_logger
        log.info("Verify checkout information form fields are displaying error message for empty data")
        log.info("Step 1: Perform complete login using valid credentials")
        self.perform_complete_login()
        log.info("User logged in successfully")
        checkout_form_page = CheckoutFormPage(self.driver)
        plp = ProductsListPage(self.driver)
        cart_page = CartPage(self.driver)
        log.info("Step 2: Add all the products to cart")
        plp.add_all_products_to_cart()
        log.info("Step 3: Navigated to cart page")
        plp.click_cart_button()
        log.info("Step 4: Clicked on checkout button")
        cart_page.click_checkout_button()
        log.info("Step 5: Click on continue button without filling any details")
        checkout_form_page.click_on_continue_button()
        log.info("Verify error message is displayed")
        try:
            assert checkout_form_page.error_exist()
            log.info("Error message is displayed")
            error = checkout_form_page.get_error_message()
            log.info("Verify error is displayed for first name")
            assert "First Name" in error
            log.info("Error is displayed for first name: "+error)
        except AssertionError:
            log.error("Error message is not displayed for first Name or no message is displayed at all")
            pytest.fail("Error message is not displayed for first Name or no message is displayed at all")
        log.info("Now enter only first Name this time ")
        checkout_form_page.enter_first_name("John")
        checkout_form_page.click_on_continue_button()
        try:
            assert checkout_form_page.error_exist()
            log.info("Error message is displayed")
            error = checkout_form_page.get_error_message()
            log.info("Verify error is displayed for last name")
            assert "Last Name" in error
            log.info("Error is displayed for last name : " + error)
        except AssertionError:
            log.error("Error message is not displayed for last Name or no message is displayed at all")
            pytest.fail("Error message is not displayed for last Name or no message is displayed at all")

        log.info("Now enter first Name and lastname this time ")
        checkout_form_page.enter_last_name("wick")
        checkout_form_page.click_on_continue_button()

        try:
            assert checkout_form_page.error_exist()
            log.info("Error message is displayed")
            error = checkout_form_page.get_error_message()
            log.info("Verify error is displayed for post code")
            assert "Postal Code" in error
            log.info("Error is displayed for Postal code : " + error)
        except AssertionError:
            log.error("Error message is not displayed for postal code or no message is displayed at all")
            pytest.fail("Error message is not displayed for postal code or no message is displayed at all")

        log.info("Now enter all the details and click on submit")
        checkout_form_page.enter_post_code("2154")
        checkout_form_page.click_on_continue_button()
        log.info("Verify user is on Checkout overview page")
        try:
            assert 'Checkout: Your Information' not in checkout_form_page.get_information_page_heading()
            log.info("User is successfully navigated to checkout overview page")
        except AssertionError:
            log.error("User is not navigated to checkout overview page")
            pytest.fail("User is not navigated to checkout overview page")

    def test_cancel(self, get_logger):
        """
        Test cancel button it should redirect to cart page
        :return: None
        """
        log = get_logger
        log.info("Verify checkout information form fields are displaying error message for empty data")
        log.info("Step 1: Perform complete login using valid credentials")
        self.perform_complete_login()
        log.info("User logged in successfully")
        checkout_form_page = CheckoutFormPage(self.driver)
        plp = ProductsListPage(self.driver)
        cart_page = CartPage(self.driver)
        log.info("Step 2: Add all the products to cart")
        plp.add_all_products_to_cart()
        log.info("Step 3: Navigated to cart page")
        plp.click_cart_button()
        log.info("Step 4: Clicked on checkout button")
        cart_page.click_checkout_button()
        log.info("Step 4: Click on cancel button")
        checkout_form_page.click_on_cancel_button()
        log.info("Verify user is on previous page that is cart page now ")
        try:
            assert cart_page.cart_heading_exist()
            log.info("user is navigated back to Cart page")
        except NoSuchElementException:
            log.error("User is not navigated to cart page")
            pytest.fail("User is not navigated to cart page")


