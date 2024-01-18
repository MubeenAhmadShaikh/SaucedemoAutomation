import pytest

from utilities.BaseClass import BaseClass
from PageObjects.ProductListPage import ProductsListPage
from PageObjects.CartPage import CartPage
from PageObjects.CheckoutFormPage import CheckoutFormPage
from PageObjects.CheckoutPage import CheckoutPage
from PageObjects.CheckoutCompletePage import CheckoutCompletePage


class TestCompleteCheckoutPage(BaseClass):

    def test_back_button(self, get_logger):
        log = get_logger
        log.info("Verify Back button on checkout completed page.")
        log.info("Step 1: Perform complete login using valid credentials")
        self.perform_complete_login()
        log.info("User logged in successfully")
        checkout_form_page = CheckoutFormPage(self.driver)
        plp = ProductsListPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        log.info("Complete the order by adding all the products")
        plp.add_all_products_to_cart()
        plp.click_cart_button()
        cart_page.click_checkout_button()
        checkout_form_page.enter_first_name("John")
        checkout_form_page.enter_last_name("Wick")
        checkout_form_page.enter_post_code(2154)
        checkout_form_page.click_on_continue_button()
        # time.sleep(5)
        checkout_page.click_on_finish_button()
        log.info("Order is finished and success message is displayed")
        checkout_complete_page = CheckoutCompletePage(self.driver)
        log.info("Now click on back button")
        checkout_complete_page.click_on_back_button()
        log.info("Verify user is navigated to inventory page")
        try:
            assert 'inventory' in self.driver.current_url
            log.info("User navigated to inventory page successfully")
        except AssertionError:
            log.error("user is not redirected to home/inventory page")
            pytest.fail("user is not redirected to home/inventory page")

    def test_success_message(self, get_logger):
        log = get_logger
        log.info("Verify success message on  checkout complete page.")
        log.info("Step 1: Perform complete login using valid credentials")
        self.perform_complete_login()
        log.info("User logged in successfully")
        checkout_form_page = CheckoutFormPage(self.driver)
        plp = ProductsListPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        plp.add_all_products_to_cart()
        plp.click_cart_button()
        cart_page.click_checkout_button()
        checkout_form_page.enter_first_name("John")
        checkout_form_page.enter_last_name("Wick")
        checkout_form_page.enter_post_code(2154)
        log.info("Complete the order by adding all the products")
        checkout_form_page.click_on_continue_button()
        # time.sleep(5)
        checkout_page.click_on_finish_button()
        checkout_complete_page = CheckoutCompletePage(self.driver)
        success_message = checkout_complete_page.get_success_message()
        try:
            assert "Thank you" in success_message
            log.info("Thank you message is displayed")
        except AssertionError:
            log.error("Thank you message is not displayed")
            pytest.fail("Thank you message is not displayed")

    def test_title(self, get_logger):
        log = get_logger
        log.info("Verify Complete title on  checkout complete page.")
        log.info("Step 1: Perform complete login using valid credentials")
        self.perform_complete_login()
        log.info("User logged in successfully")
        checkout_form_page = CheckoutFormPage(self.driver)
        plp = ProductsListPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        plp.add_all_products_to_cart()
        plp.click_cart_button()
        cart_page.click_checkout_button()
        checkout_form_page.enter_first_name("John")
        checkout_form_page.enter_last_name("Wick")
        checkout_form_page.enter_post_code(2154)
        checkout_form_page.click_on_continue_button()
        log.info("Complete the order by adding all the products")
        # time.sleep(5)
        checkout_page.click_on_finish_button()
        checkout_complete_page = CheckoutCompletePage(self.driver)
        page_title = checkout_complete_page.get_title()
        try:
            log.info("Check Complete! is displayed on checkout complete page")
            assert 'Complete!' in page_title
            log.info("Complete! is displayed")
        except AssertionError:
            log.error("Complete! is not displayed as title on checkout complete page")
            pytest.fail("Complete! is not displayed as title on checkout complete page")
