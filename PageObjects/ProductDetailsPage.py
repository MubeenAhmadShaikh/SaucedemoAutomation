from selenium.webdriver.common.by import By
import random
from PageObjects.Page import Page
from PageObjects.ProductListPage import ProductsListPage


class ProductDetailsPage(Page):

    # product details page element locators
    product_name_locator = (By.CSS_SELECTOR, ".inventory_details_name")
    product_price_locator = (By.CSS_SELECTOR, ".inventory_details_price")
    add_to_cart_button = (By.XPATH, "//button[text()='Add to cart']")
    remove_button = (By.XPATH, "//button[text()='Remove']")
    back_to_plp_button = (By.CSS_SELECTOR, "#back-to-products")
    heading_locator = (By.CSS_SELECTOR, ".title")
    cart_locator = (By.CSS_SELECTOR, ".shopping_cart_link")
    cart_items = (By.XPATH, "//div[@class='cart_list']/div[@class='cart_item']")

    # get [element] methods
    def get_product_name(self):
        """ Returns the product name of active webdriver page"""
        return self.driver.find_element(*ProductDetailsPage.product_name_locator).text

    def get_product_price(self):
        """ Returns the product price of active webdriver page"""
        return self.driver.find_element(*ProductDetailsPage.product_price_locator).text

    def get_product_image(self):
        """ Validate the product image is same is displayed on PLP"""
        pass

    def get_list_of_cart_items(self):
        return self.driver.find_elements(*ProductDetailsPage.cart_items)

    #  click [element] methods
    def click_back_to_products(self):
        """ Click on back button for PLP"""
        self.driver.find_element(*ProductDetailsPage.back_to_plp_button).click()

    def click_add_to_cart(self):
        """Click on add to cart button"""
        self.driver.find_element(*ProductDetailsPage.add_to_cart_button).click()

    def click_remove_button(self):
        """Click on remove button"""
        self.driver.find_element(*ProductDetailsPage.remove_button).click()

    def click_on_cart_button(self):
        self.driver.find_element(*ProductDetailsPage.cart_locator).click()

    # complete action methods
    def select_a_random_product(self):
        plp_page = ProductsListPage(self.driver)
        all_products = plp_page.get_all_products()
        if all_products:
            product = random.choice(all_products)
            product_name_link = product.find_element(By.CSS_SELECTOR, ".inventory_item_name")
            product_name = product_name_link.text
            product_price = product.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
            product_name_link.click()
            return product_name, product_price, product

    def add_random_product_to_cart(self):
        self.select_a_random_product()
        self.click_on_cart_button()
        cart_items = self.get_list_of_cart_items()
        if len(cart_items) == 0:
            self.driver.back()
            self.click_add_to_cart()

    def product_heading_exist(self):
        return True if self.driver.find_element(*ProductDetailsPage.heading_locator) else False
