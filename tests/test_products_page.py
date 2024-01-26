import allure
import pytest
from allure_commons.types import AttachmentType
from PageObjects.ProductListPage import ProductsListPage
from utilities.BaseClass import BaseClass


class TestProductsPage(BaseClass):

    def test_sort_a_to_z(self, get_logger):
        """ For validating the filter for products with A to Z filter"""
        log = get_logger
        log.info("Verify user is able to sort the products using a-to-z filter")
        log.info("Step 1: Perform complete login")
        self.perform_complete_login()
        products_page = ProductsListPage(self.driver)
        products_before_sort = []
        products_after_sort = []
        for product in products_page.get_all_products_name():
            products_before_sort.append(product.text)
        log.info("Step 2: Once user is on home page sort the products with a-to-z filter")
        products_page.sort_products_a_to_z()
        for product in products_page.get_all_products_name():
            products_after_sort.append(product.text)
        try:
            assert products_after_sort == products_before_sort
            log.info("Products are sorted successfully")
        except AssertionError:
            log.error("Products are not sorted")
            allure.attach(self.driver.get_screenshot_as_png(), "evidence", attachment_type=AttachmentType.PNG)
            pytest.fail("Products are not sorted as expected")

    def test_sort_z_to_a(self, get_logger):
        """ For validating the filter for products with Z to A filter"""
        log = get_logger
        log.info("Verify user is able to sort the products using z-to-a filter")
        log.info("Step 1: Perform complete login")
        self.perform_complete_login()
        log.info("User is logged in")
        products_page = ProductsListPage(self.driver)
        products_before_sort = []
        products_after_sort = []
        for product in products_page.get_all_products_name():
            products_before_sort.append(product.text)
        log.info("Step 2: Sort the products from z-to-a")
        products_page.sort_products_z_to_a()
        for product in products_page.get_all_products_name():
            products_after_sort.append(product.text)
        try:
            assert products_after_sort == products_before_sort[::-1]
            log.info("Products are sorted from z-to-a")
        except AssertionError:
            log.error("Products are not sorted in z-to-a")
            allure.attach(self.driver.get_screenshot_as_png(), "evidence", attachment_type=AttachmentType.PNG)
            pytest.fail("Products are not sorted as expected")

    def test_sort_low_to_high(self, get_logger):
        """ For validating the filter for products with low to high filter"""
        log = get_logger
        log.info("Verify user is able to sort the products using low-to-high filter")
        log.info("Step 1: Perform complete login")
        self.perform_complete_login()
        log.info("User is logged in")
        products_page = ProductsListPage(self.driver)
        products_before_sort = []
        products_after_sort = []
        for product in products_page.get_all_product_prices():
            products_before_sort.append(product.text[1:])
        log.info("Step 2: Sort the products from low-to-high price")
        products_page.sort_products_low_to_high()
        for product in products_page.get_all_product_prices():
            products_after_sort.append(product.text[1:])
        try:
            assert products_after_sort == sorted(products_before_sort, key=float)
            log.info("Products are sorted from low-to-high")
        except AssertionError:
            log.error("Products are not sorted from low-to-high")
            allure.attach(self.driver.get_screenshot_as_png(), "evidence", attachment_type=AttachmentType.PNG)
            pytest.fail("Products are not sorted from low-to-high")

    def test_sort_high_to_low(self, get_logger):
        """ For validating the filter for products with high to low filter"""
        log = get_logger
        log.info("Verify user is able to sort the products using high-to-low filter")
        log.info("Step 1: Perform complete login")
        self.perform_complete_login()
        log.info("User logged in successfully")
        products_page = ProductsListPage(self.driver)
        products_before_sort = []
        products_after_sort = []
        for product in products_page.get_all_product_prices():
            products_before_sort.append(product.text[1:])
        log.info("Step 2: Sort the product using high-to-low filter")
        products_page.sort_products_high_to_low()
        for product in products_page.get_all_product_prices():
            products_after_sort.append(product.text[1:])
        try:
            assert products_after_sort == sorted(products_before_sort, key=float, reverse=True)
            log.info("Products are sorted successfully from high-to-low pricing")
        except AssertionError:
            log.error("Products are not sorted high-to-low in pricing")
            allure.attach(self.driver.get_screenshot_as_png(), "evidence", attachment_type=AttachmentType.PNG)
            pytest.fail("Products are not sorted high-to-low in pricing")

    def test_add_to_cart_all_products(self, get_logger):
        """ Validating the add to cart button on PLP"""
        log = get_logger
        log.info("Verify user is able to add all the present product to cart")
        log.info("Step 1: Perform complete login")
        self.perform_complete_login()
        log.info("User logged in successfully")
        products_page = ProductsListPage(self.driver)
        log.info("Step 2: Add all the products to cart")
        products_page.add_all_products_to_cart()
        added_products = products_page.get_number_of_cart_items()
        all_products = products_page.get_all_products()
        try:
            assert added_products == len(all_products)
            log.info("Successfully added all the products to cart")
        except AssertionError:
            log.error("Unable to add all the products to cart")
            allure.attach(self.driver.get_screenshot_as_png(), "evidence", attachment_type=AttachmentType.PNG)
            pytest.fail("Unable to add all the products to cart")
        products_page.empty_cart()

    def test_remove_buttons(self, get_logger):
        """ Testing the remove button in PLP after adding product to cart. """
        log = get_logger
        log.info("Verify remove buttons on home page for all the products are functioning properly")
        log.info("Step 1: Perform complete login")
        self.perform_complete_login()
        log.info("User logged in successfully")
        products_page = ProductsListPage(self.driver)
        products_page.empty_cart()
        remove_buttons = products_page.get_all_remove_buttons()
        log.info("Check no remove buttons should be displayed at start")
        assert len(remove_buttons) == 0
        log.info("No remove buttons are present")
        log.info("Adding all the products to cart")
        products_page.add_all_products_to_cart()
        all_products = products_page.get_all_products()
        products_in_cart = products_page.get_number_of_cart_items()
        try:
            assert len(all_products) == products_in_cart
            log.info("Added all the products to cart")
            log.info("Removing products using remove button")
            products_page.empty_cart()
            assert len(products_page.get_all_remove_buttons()) == 0
            log.info("All the remove buttons are functioning properly")
        except AssertionError:
            log.error("Remove buttons are not functioning properly")
            allure.attach(self.driver.get_screenshot_as_png(), "evidence", attachment_type=AttachmentType.PNG)
            pytest.fail("Remove buttons are not functioning properly")

    def test_add_to_cart_by_title(self, get_logger):
        """ Validating the adding to cart functionality by giving a name of the product"""
        log = get_logger
        log.info("Verify user is able to add the product to cart by its title")
        log.info("Step 1: Perform complete login")
        self.perform_complete_login()
        log.info("User logged in successfully")
        products_page = ProductsListPage(self.driver)
        log.info("Step 2: Provide the product title for adding to cart")
        products = products_page.get_list_of_products_by_title("Sauce Labs Backpack")
        log.info("title provided for product: Sauce Labs Backpack")
        log.info("Step 3: Add product to cart with title Sauce Labs Backpack")
        products_page.add_to_cart_product_by_title("Sauce Labs Backpack")
        try:
            assert len(products) == products_page.get_number_of_cart_items()
            log.info("Product with given title is added to cart")
        except AssertionError:
            log.error("Product with given title is not added to cart")
            allure.attach(self.driver.get_screenshot_as_png(), "evidence", attachment_type=AttachmentType.PNG)
            pytest.fail("Product with given title is not added to cart")
        products_page.empty_cart()

    def test_add_to_cart_by_price(self, get_logger):
        """ Validating the adding to cart functionality by giving the price of the product"""
        log = get_logger
        log.info("Verify user is able to add the product to cart by its price")
        log.info("Step 1: Perform complete login")
        self.perform_complete_login()
        log.info("User logged in successfully")
        products_page = ProductsListPage(self.driver)
        log.info("Step 2: Provide the product price for adding to cart")
        products = products_page.get_list_of_products_by_price("7.99")
        log.info("title provided for product: 7.99")
        # enter price without $ sign
        log.info("Step 3: Add product to cart with price 7.99")
        products_page.add_to_cart_product_by_price("7.99")
        try:
            assert len(products) == products_page.get_number_of_cart_items()
            log.info("Products with the given price is added to cart")
        except AssertionError:
            log.error("Product with given price is not added to cart")
            allure.attach(self.driver.get_screenshot_as_png(), "evidence", attachment_type=AttachmentType.PNG)
            pytest.fail("Product with given price is not added to cart")
        products_page.empty_cart()
