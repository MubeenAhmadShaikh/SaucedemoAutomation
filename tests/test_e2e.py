import time

import pytest
from PageObjects.CartPage import CartPage
from selenium.webdriver.common.by import By

from PageObjects.ProductListPage import ProductsListPage
from utilities.BaseClass import BaseClass
from PageObjects.CheckoutFormPage import CheckoutFormPage
from PageObjects.CheckoutPage import CheckoutPage


class TestE2E(BaseClass):

    def e2e_purchase(self, scenario, get_logger):
        self.driver.implicitly_wait(4)
        self.driver.get('https://www.saucedemo.com/')
        # self.loginUser()
        log = get_logger
        log.info("Verify end to end purchasing of the product.")
        self.perform_complete_login()
        products_list_page = ProductsListPage(self.driver)

        if scenario == 'purchase_all_product':
            log.info("Verify user is able to complete the end to end purchasing of all the product.")
            log.info("Add all the products to cart")
            products_list_page.add_all_products_to_cart()
            cart_icons = products_list_page.get_number_of_cart_items()
            try:
                assert cart_icons == len(products_list_page.get_all_products())
                log.info("All products added to cart")
            except AssertionError:
                log.error("All products are not added to cart")
                pytest.fail("All products are not added to cart")
        elif scenario == 'purchase_lowest_price_product':
            log.info("Verify user is able to complete the end to end purchasing of lowest price product")
            log.info("Add lowest price product to cart")
            self.select_option_by_text(products_list_page.get_sort_menu(), "Price (low to high)")
            prices = products_list_page.get_all_product_prices()
            lowest_price = prices[0].text
            products = products_list_page.add_to_cart_product_by_price(lowest_price[1:])
            cart_icons = products_list_page.get_number_of_cart_items()
            log.info("Verify lowest price product added to cart if two products have same price 2 products will"
                     " be added")
            try:
                assert cart_icons == len(products)
                log.info("Lowest price products are added to cart")
            except AssertionError:
                log.error("lowest price products are not added to cart")
                pytest.fail("lowest price products are not added to cart")

        elif scenario == 'purchase_highest_price_product':
            log.info("Verify user is able to complete the end to end purchasing of highest price product")
            log.info("Add highest price product to cart")
            self.select_option_by_text(products_list_page.get_sort_menu(), "Price (high to low)")
            prices = products_list_page.get_all_product_prices()
            highest_price = prices[0].text
            products = products_list_page.add_to_cart_product_by_price(highest_price[1:])
            cart_icons = products_list_page.get_number_of_cart_items()
            log.info("Verify highest price product added to cart if two products have same price 2 products will"
                     " be added")
            try:
                assert cart_icons == len(products)
                log.info("highest price products are added to cart")
            except AssertionError:
                log.error("highest price products are not added to cart")
                pytest.fail("highest price products are not added to cart")

        elif scenario == 'purchase_mid_price_product':
            log.info("Verify user is able to complete the end to end purchasing of medium price product")
            log.info("Add medium price product to cart")
            self.select_option_by_text(products_list_page.get_sort_menu(), "Price (high to low)")
            prices = products_list_page.get_all_product_prices()
            avg_price = prices[int(len(prices)/2)].text
            print(avg_price)
            products = products_list_page.add_to_cart_product_by_price(avg_price[1:])
            time.sleep(2)
            cart_icons = products_list_page.get_number_of_cart_items()
            log.info("Verify medium price product added to cart if two products have same price 2 products will"
                     " be added")
            try:
                assert cart_icons == len(products)
                log.info("medium price products are added to cart")
            except AssertionError:
                log.error("medium price products are not added to cart")
                pytest.fail("medium price products are not added to cart")

        elif scenario == "purchase_product_by_name":
            log.info("Verify user is able to complete the end to end purchasing a product by its name")
            log.info("Add the product with the name mentioned to cart")
            products = products_list_page.add_to_cart_product_by_title("Sauce Labs Onesie")
            cart_icons = products_list_page.get_number_of_cart_items()
            log.info("Verify product is added to cart")
            try:
                assert cart_icons == len(products)
                log.info("product is added to cart")
            except AssertionError:
                log.error("product is not added to cart")
                pytest.fail("product is not added to cart")
        elif scenario == "purchase_product_by_price":
            log.info("Verify user is able to complete the end to end purchasing a product by its price")
            log.info("Add the product with the price mentioned to cart")
            products = products_list_page.add_to_cart_product_by_price("29.99")
            cart_icons = products_list_page.get_number_of_cart_items()
            log.info("Verify product is added to cart")
            try:
                assert cart_icons == len(products)
                log.info("product is added to cart")
            except AssertionError:
                log.error("product is not added to cart")
                pytest.fail("product is not added to cart")

        # cart_page = products_list_page.getCartButton()
        products_list_page.click_cart_button()
        cart_page = CartPage(self.driver)
        assert 'cart' in self.driver.current_url
        cart_page.click_checkout_button()
        checkout_form_page = CheckoutFormPage(self.driver)
        # Cart page validations
        assert ('checkout' and 'one') in self.driver.current_url
        checkout_form_page.enter_first_name("John")
        checkout_form_page.enter_last_name("Wick")
        checkout_form_page.enter_post_code("2154")
        checkout_form_page.click_on_continue_button()  # Changed
        checkout_page = CheckoutPage(self.driver)
        size = lambda x: self.driver.execute_script('return document.body.parentNode.scroll' + x)
        self.driver.set_window_size(size('Width'), size('Height'))  # May need manual adjustment
        self.driver.find_element(By.TAG_NAME, 'body').screenshot('images/checkout_page.png')

        assert ('checkout' and 'two') in self.driver.current_url
        # Checkout final page validations
        checkout_complete_page = checkout_page.click_on_finish_button()
        # checkout_complete_page = CheckoutCompletePage(self.driver)
        assert ('checkout' and 'complete') in self.driver.current_url
        time.sleep(3)
        # Checkout final page validations
        success_message = checkout_complete_page.get_success_message()
        assert "Thank you" in success_message
        checkout_complete_page.click_on_back_button()
        assert "inventory" in self.driver.current_url

    def test_purchase_all_products(self, get_logger):
        self.e2e_purchase("purchase_all_product", get_logger)
     
    def test_purchase_lowest_price_product(self, get_logger):
        self.e2e_purchase("purchase_lowest_price_product", get_logger)
     
    def test_purchase_highest_price_product(self, get_logger):
        self.e2e_purchase("purchase_highest_price_product", get_logger)
     
    def test_purchase_medium_price_product(self, get_logger):
        self.e2e_purchase("purchase_mid_price_product", get_logger)

    def test_purchase_product_by_title(self, get_logger):
        self.e2e_purchase("purchase_product_by_name", get_logger)
     
    def test_purchase_product_by_price(self, get_logger):
        self.e2e_purchase("purchase_product_by_price", get_logger)
