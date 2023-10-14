import random
import time

import pytest
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass
from pageObjects.ProductDetailsPage import ProductDetailsPage
from pageObjects.ProductListPage import ProductsListPage
from pageObjects.CartPage import CartPage


class TestCartPage(BaseClass):

    def test_cart_heading(self, get_logger):
        """ Validating if Your cart heading exist"""
        log = get_logger
        log.info("Verify cart page heading is displayed as expected")
        log.info("Step 1: Perform complete login using valid credentials")
        self.perform_complete_login()
        log.info("User logged in successfully")
        cart_page = CartPage(self.driver)
        pdp = ProductDetailsPage(self.driver)
        log.info("Step 2: Add a product to cart")
        pdp.click_on_cart_button()
        log.info("Verify on cart page the heading of Cart is displayed")
        try:
            assert cart_page.cart_heading_exist()
            log.info("Cart page heading is displayed as expected")
        except AssertionError:
            log.error("Cart page heading is not displayed")
            pytest.fail("Cart page heading is not displayed")

    def test_checkout_button(self, get_logger):
        """ Validating the checkout button"""
        log = get_logger
        log.info("Verify checkout button is working as expected")
        log.info("Step 1: Perform complete login using valid credentials")
        self.perform_complete_login()
        log.info("User logged in successfully")
        cart_page = CartPage(self.driver)
        pdp = ProductDetailsPage(self.driver)
        log.info("Step 2: Add a product to cart")
        pdp.click_on_cart_button()
        try:
            assert cart_page.cart_heading_exist()
            log.info("Cart page heading is displayed as expected")
            cart_page.click_checkout_button()
            try:
                assert cart_page.checkout_page_heading_exist()
                log.info("Checkout button is working as expected")
            except AssertionError:
                log.error("Checkout button is not functioning properly")
                pytest.fail("Checkout button is not functioning properly")
        except AssertionError:
            log.error("Cart page heading is not displayed")
            pytest.fail("Cart page heading is not displayed")

    def test_continue_shopping(self, get_logger):
        log = get_logger
        log.info("Verify checkout button is working as expected")
        log.info("Step 1: Perform complete login using valid credentials")
        self.perform_complete_login()
        log.info("User logged in successfully")
        cart_page = CartPage(self.driver)
        pdp = ProductDetailsPage(self.driver)
        log.info("Step 2: Add a product to cart")
        pdp.click_on_cart_button()
        log.info("Step 3: Proceed with continue shopping")
        cart_page.click_continue_shopping()
        pdp = ProductDetailsPage(self.driver)
        plp = ProductsListPage(self.driver)
        log.info("Step 3: Verify user is on PLP page")
        plp_page_heading = plp.get_page_heading()
        try:
            assert plp_page_heading
            self.captureScreenShot("images/Before_adding.png")
            log.info("User is on PLP and heading of 'Products' is displayed")
            log.info("Step 4: Now add all the products to cart")
            plp.add_all_products_to_cart()
            log.info("Step 5: Click on cart button")
            pdp.click_on_cart_button()
            current_items_in_cart = len(cart_page.get_cart_items())
            total_cart_items = plp.get_number_of_cart_items()
            log.info("Verify actual cart items are equal to the ")
            try:
                assert current_items_in_cart == total_cart_items
                log.info("cart items are same as we have added")
                self.captureScreenShot("images/continue.png")
            except AssertionError:
                log.error("Cart items are not same as selected")
                pytest.fail("Cart items are not same as selected")
        except AssertionError:
            log.error("User is not navigate to PLP after clicking on Continue shopping")
            pytest.fail("User is not navigate to PLP after clicking on Continue shopping")

    def test_remove_from_cart(self, get_logger):
        log = get_logger
        log.info("Verify checkout button is working as expected")
        log.info("Step 1: Perform complete login using valid credentials")
        self.perform_complete_login()
        log.info("User logged in successfully")
        cart_page = CartPage(self.driver)
        plp = ProductsListPage(self.driver)
        pdp = ProductDetailsPage(self.driver)
        log.info("Step 2: Select all product and add to cart")
        plp.add_all_products_to_cart()
        log.info("Step 3: Click on cart button")
        pdp.click_on_cart_button()
        cart_items = cart_page.get_cart_items()
        log.info("Verify if cart items are present then validate the remove button functionality")
        if cart_items:
            log.info("Select a random product from the cart")
            random_product = random.choice(cart_items)
            self.captureScreenShot("images/cart.png")
            log.info("Remove that product using remove button")
            cart_page.remove_cart_item(random_product)
            time.sleep(3)
            log.info("Get the current items in number")
            current_cart_items = cart_page.get_cart_items()
            # Checking if cart item is removed from cart and list is updated
            try:
                assert len(current_cart_items) < len(cart_items)
                log.info("current cart items are less than actual once so remove button is working fine.")
                # Checking the cart item numbers are updated
                try:
                    assert plp.get_number_of_cart_items() == len(current_cart_items)
                    log.info("Cart items on PLP and actual cart have same data")
                except AssertionError:
                    log.error("Error or mismatch in cart items on PLP and cart")
            except AssertionError:
                log.info("cart item count is not as expected")
                pytest.fail("cart item count is not as expected")