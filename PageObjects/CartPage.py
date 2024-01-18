from selenium.webdriver.common.by import By

from PageObjects.Page import Page


class CartPage(Page):

    heading_locator = (By.CSS_SELECTOR, ".title")
    checkout_button = (By.ID, "checkout")
    continue_shopping_button = (By.XPATH, "//button[@id='continue-shopping']")
    checkout_page_heading = (By.CSS_SELECTOR, ".title")
    cart_items = (By.CSS_SELECTOR, ".cart_item")
    remove_button = (By.XPATH, "/button[text()='Remove']")

    def cart_heading_exist(self):
        cart_heading = self.driver.find_element(*CartPage.heading_locator).text
        return True if 'Cart' in cart_heading else False

    def click_checkout_button(self):
        self.driver.find_element(*CartPage.checkout_button).click()

    def click_continue_shopping(self):
        self.driver.find_element(*CartPage.continue_shopping_button).click()

    def checkout_page_heading_exist(self):
        checkout_page_heading = self.driver.find_element(*CartPage.checkout_page_heading)
        return True if checkout_page_heading else False

    def get_cart_items(self):
        return self.driver.find_elements(*CartPage.cart_items)

    def remove_cart_item(self, item):
        remove_button = item.find_element(By.XPATH, "//button[text()='Remove']")
        remove_button.click()

