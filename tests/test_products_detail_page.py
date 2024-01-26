import time

import allure
import pytest
from allure_commons.types import AttachmentType

from PageObjects.ProductDetailsPage import ProductDetailsPage
from PageObjects.ProductListPage import ProductsListPage
from utilities.BaseClass import BaseClass
from selenium.common.exceptions import NoSuchElementException


class TestProductsDetailPage(BaseClass):

    def test_product_name_and_price(self, get_logger):
        log = get_logger
        log.info("Verify the names and prices of the products are in sync on PLP and PDP")
        log.info("Step 1: Perform the completed login using valid credentials")
        self.perform_complete_login()
        log.info("User is logged in successfully")
        product_details_page = ProductDetailsPage(self.driver)
        log.info("Step 2: Select a random product from PLP")
        product_name_on_plp, product_price_on_plp, product_on_plp = product_details_page.select_a_random_product()
        log.info("Product selected on PLP having name as "+product_name_on_plp+" and price as "+product_price_on_plp)
        product_name_on_pdp = product_details_page.get_product_name()
        product_price_on_pdp = product_details_page.get_product_price()
        log.info("Product on PDP having name as "+product_name_on_pdp+" and price as "+product_price_on_pdp)
        log.info("Step 3: Verify the names and prices of the selected product are in sync across the PDP and PLP pages")
        try:
            assert product_name_on_pdp == product_name_on_plp
            assert product_price_on_pdp == product_price_on_plp
            log.info("Product name and price on PLP and PDP are in sync")
        except (AssertionError, NoSuchElementException):
            log.error("Product name or price is not in sync on PDP and PLP")
            allure.attach(self.driver.get_screenshot_as_png(), "evidence", attachment_type=AttachmentType.PNG)
            pytest.fail("Product name or price is not in sync on PDP and PLP")

    def test_back_to_plp(self, get_logger):
        log = get_logger
        log.info("Verify back to PLP button on product details page.")
        log.info("Step 1: Perform complete login using valid credentials")
        self.perform_complete_login()
        log.info("User is logged in successfully")
        product_details_page = ProductDetailsPage(self.driver)
        log.info("Step 2: Select a random product on PLP ")
        product_details_page.select_a_random_product()
        log.info("Verify product is selected and redirected to PDP ")
        product_details_page.click_back_to_products()
        log.info("Step 3: Click on back to products button")
        try:
            assert product_details_page.product_heading_exist()
            log.info("Products listing page is displayed with the 'Products' heading")
        except (AssertionError, NoSuchElementException):
            log.error("'Products' heading is not displayed and user is not redirected to PLP")
            allure.attach(self.driver.get_screenshot_as_png(), "evidence", attachment_type=AttachmentType.PNG)
            pytest.fail("'Products' heading is not displayed and user is not redirected to PLP")

    def test_add_to_cart(self, get_logger):
        log = get_logger
        log.info("Verify add to cart functionality is working as expected from PDP")
        log.info("Step 1: Perform complete login with valid creds")
        self.perform_complete_login()
        log.info("User is logged in successfully")
        cart_items = 0
        product_details_page = ProductDetailsPage(self.driver)
        product_plp = ProductsListPage(self.driver)
        product_plp.empty_cart()
        log.info("Step 2: Select a random product and navigate to its PDP and click on add to cart")
        first_product_name, first_product_price, first_product = product_details_page.select_a_random_product()
        product_details_page.click_add_to_cart()
        log.info("Item added to the cart")
        cart_items += 1
        log.info("Step 3: Get the actual number of cart items")
        actual_cart_items = product_plp.get_number_of_cart_items()
        try:
            assert actual_cart_items == cart_items
            log.info("add to cart on PDP is working as expected")
            log.info("Navigate back to the PLP page and select a different product")
            product_details_page.click_back_to_products()
            second_product_name, second_product_price, second_product = product_details_page.select_a_random_product()
            if first_product != second_product:
                log.info("second product is selected")
                log.info("Click on Add to cart on its PDP")
                product_details_page.click_add_to_cart()
                cart_items += 1
                log.info("Verify cart items are increased by 1")
                actual_cart_items = product_plp.get_number_of_cart_items()
                assert actual_cart_items == cart_items
                product_details_page.click_remove_button()
                cart_items -= 1
                actual_cart_items = product_plp.get_number_of_cart_items()
                assert actual_cart_items == cart_items
        except (AssertionError, NoSuchElementException):
            log.error("Add to cart is not working properly")
            allure.attach(self.driver.get_screenshot_as_png(), "evidence", attachment_type=AttachmentType.PNG)
            pytest.fail("Add to cart is not working properly")

    def test_remove_button(self, get_logger):
        log = get_logger
        log.info("Verify remove button functionality is working as expected from PDP")
        log.info("Step 1: Perform complete login with valid creds")
        self.perform_complete_login()
        log.info("User is logged in successfully")
        cart_items = 0
        product_details_page = ProductDetailsPage(self.driver)
        product_plp = ProductsListPage(self.driver)
        product_plp.empty_cart()
        log.info("Step 2: Add any random product to cart")
        product_details_page.add_random_product_to_cart()
        cart_items += 1
        log.info("Step 3: Click on remove button on PDP")
        product_details_page.click_remove_button()
        cart_items -= 1
        actual_cart_items = product_plp.get_number_of_cart_items()
        try:
            assert actual_cart_items == cart_items
            log.info("Remove button is working as expected")
        except (AssertionError, NoSuchElementException):
            log.error("Remove button is not working as expected")
            allure.attach(self.driver.get_screenshot_as_png(), "evidence", attachment_type=AttachmentType.PNG)
            pytest.fail("Remove button is not working as expected")
