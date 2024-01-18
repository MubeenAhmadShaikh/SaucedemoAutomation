import time

import pytest

from PageObjects.CartPage import CartPage
from PageObjects.CheckoutFormPage import CheckoutFormPage
from PageObjects.ProductDetailsPage import ProductDetailsPage
from PageObjects.ProductListPage import ProductsListPage
from utilities.BaseClass import BaseClass


class TestCheckoutOverviewPage(BaseClass):

    def test_checkout_all_items(self, get_logger):
        """
        This test will validate by checking out with all the present items and checking:
        Order total
        Item total
        Tax
        Quantities
        """
        log = get_logger
        log.info("Verify products, item total, total on checkout overview page and "
                 "Thank you message after submitting the order for purchasing all the products.")
        log.info("Step 1: Perform complete login using valid credentials")
        self.perform_complete_login()
        log.info("User logged in successfully")
        checkout_form_page = CheckoutFormPage(self.driver)
        plp = ProductsListPage(self.driver)
        cart_page = CartPage(self.driver)
        log.info("Step 2: Add all the products to cart")
        plp.add_all_products_to_cart()
        log.info("Step 3: Navigated to checkout overview page")
        checkout_overview_page = checkout_form_page.navigate_to_checkout_overview_page(
            plp, cart_page, checkout_form_page)
        log.info("Capture receipt")
        checkout_overview_page.capture_receipt("images/receipt_all_items.png")
        log.info("Verify item total, total and products on checkout overview page")
        try:
            assert plp.get_number_of_cart_items() == checkout_overview_page.get_quantities()
            log.info("The number of products on cart page and on checkout overview page are same")
            assert checkout_overview_page.calculate_item_total() == checkout_overview_page.get_item_total()
            log.info("The item total is calculated correctly")
            assert checkout_overview_page.get_total() == checkout_overview_page.calculate_total()
            log.info("The Total amount is also calculated correctly")
            log.info("Click on Finish button")
            checkout_overview_page.click_on_finish_button()
        except AssertionError:
            log.error("There is unexpected item total, total or products mentioned on checkout overview page")
            pytest.fail("There is unexpected item total, total or products mentioned on checkout overview page")
        try:
            assert 'Thank you' in checkout_overview_page.get_thankyou_message()
            log.info("Thank you message is displayed")
        except AssertionError:
            log.error("Thank you message is not displayed")
            pytest.fail("Thank You message is not displayed")

    def test_checkout_one_item(self, get_logger):
        """
        This test will validate by checking out with single item either by name or price and checking:
        Order total
        Item total
        Tax
        Quantities
        """
        log = get_logger
        log.info("Verify products, item total, total on checkout overview page and "
                 "Thank you message after submitting the order for purchasing a single products.")
        log.info("Step 1: Perform complete login using valid credentials")
        self.perform_complete_login()
        log.info("User logged in successfully")
        checkout_form_page = CheckoutFormPage(self.driver)
        plp = ProductsListPage(self.driver)
        cart_page = CartPage(self.driver)
        price = '15.99'
        log.info("Add the product to cart with price "+price)
        plp.add_to_cart_product_by_price(price)
        # plp.add_to_cart_product_by_title('')
        log.info("Navigate to checkout overview page")
        checkout_overview_page = checkout_form_page.navigate_to_checkout_overview_page(
            plp, cart_page, checkout_form_page)
        self.scroll_to_bottom()
        log.info("Capture the receipt")
        checkout_overview_page.capture_receipt("images/receipt_single_item.png")
        try:
            assert plp.get_number_of_cart_items() == checkout_overview_page.get_quantities()
            log.info("The number of products on cart page and on checkout overview page are same")
            assert checkout_overview_page.calculate_item_total() == checkout_overview_page.get_item_total()
            log.info("The item total is calculated correctly")
            assert checkout_overview_page.get_total() == checkout_overview_page.calculate_total()
            log.info("The Total amount is also calculated correctly")
            log.info("Click on Finish button")
            checkout_overview_page.click_on_finish_button()
        except AssertionError:
            log.error("There is unexpected item total, total or products mentioned on checkout overview page")
            pytest.fail("There is unexpected item total, total or products mentioned on checkout overview page")
        try:
            assert 'Thank you' in checkout_overview_page.get_thankyou_message()
            log.info("Thank you message is displayed")
        except AssertionError:
            log.error("Thank you message is not displayed")
            pytest.fail("Thank You message is not displayed")

    def test_cancel_button(self, get_logger):
        """
        This test will check the functionality of cancel button.
        """
        log = get_logger
        log.info("Verify cancel button on checkout overview page.")
        log.info("Step 1: Perform complete login using valid credentials")
        self.perform_complete_login()
        log.info("User logged in successfully")
        checkout_form_page = CheckoutFormPage(self.driver)
        plp = ProductsListPage(self.driver)
        cart_page = CartPage(self.driver)
        price = '15.99'
        log.info("Add the product to cart with price " + price)
        plp.add_to_cart_product_by_price(price)
        log.info("Navigate to checkout overview page")
        checkout_overview_page = (checkout_form_page.navigate_to_checkout_overview_page
                                  (plp, cart_page, checkout_form_page))
        log.info("Click on cancel button")
        checkout_overview_page.click_on_cancel_button()
        log.info("Verify user is navigated back to the home page with 'Products' heading")
        try:
            assert 'Products' in plp.get_page_heading()
            log.info(" user is on home page and Products heading is displayed")
        except AssertionError:
            log.error("User is not on home page or Products title is not displayed")
            pytest.fail("User is not on home page or Products title is not displayed")

    def test_checkout_with_zero_total(self, get_logger):
        log = get_logger
        log.info("Verify user is not able to proceed if cart is empty.")
        log.info("Step 1: Perform complete login using valid credentials")
        self.perform_complete_login()
        log.info("User logged in successfully")
        cart_page = CartPage(self.driver)
        pdp = ProductDetailsPage(self.driver)
        plp = ProductsListPage(self.driver)
        checkout_form_page = CheckoutFormPage(self.driver)
        log.info("Step 2: Add a product to cart")
        pdp.add_random_product_to_cart()
        pdp.click_remove_button()
        pdp.click_on_cart_button()
        cart_page.click_checkout_button()
        checkout_overview_page = (checkout_form_page.navigate_to_checkout_overview_page
                                  (plp, cart_page, checkout_form_page))
        try:
            assert checkout_overview_page.get_total() == 0.0
            checkout_overview_page.click_on_finish_button()
            assert checkout_overview_page.checkout_overview_heading_exist()
            log.info("User is unable to proceed with having order total as 0")
        except AssertionError:
            log.error("User is able to proceed with finish order when total is 0")
            pytest.fail("User is able to proceed with finish order when total is 0")
