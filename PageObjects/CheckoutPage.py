from selenium.webdriver.common.by import By
from PageObjects.CheckoutCompletePage import CheckoutCompletePage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    # Element locators for Checkout page
    item_total = (By.CSS_SELECTOR, "div[class='summary_subtotal_label']")
    tax = (By.CSS_SELECTOR, "div[class='summary_tax_label']")
    total = (By.CSS_SELECTOR, ".summary_total_label")
    item_price_locator = (By.CSS_SELECTOR, ".inventory_item_price")
    quantity_locator = (By.CSS_SELECTOR, ".cart_quantity")
    cancel_button = (By.ID, "cancel")
    finish_button = (By.ID, "finish")
    thankyou_message = (By.CSS_SELECTOR, ".complete-header")
    receipt_section = (By.CSS_SELECTOR, ".summary_info")
    title_heading = (By.CLASS_NAME, "title")

    # Get [element] methods
    def get_item_total(self):
        total_text = self.driver.find_element(*CheckoutPage.item_total).text
        return float(total_text.split("$")[1])

    def get_tax(self):
        tax = self.driver.find_element(*CheckoutPage.tax).text
        return float(tax.split('$')[1])

    def get_total(self):
        total = self.driver.find_element(*CheckoutPage.total).text
        return float(total.split('$')[1])

    def get_thankyou_message(self):
        return self.driver.find_element(*CheckoutPage.thankyou_message).text

    def get_price_of_all_items(self):
        prices = self.driver.find_elements(*CheckoutPage.item_price_locator)
        final_prices = []
        for price in prices:
            final_prices.append(price.text[1:])
        return final_prices

    def get_quantities(self):
        quantities = self.driver.find_elements(*CheckoutPage.quantity_locator)
        count_of_products = 0
        for qty in quantities:
            count_of_products += int(qty.text)
        return count_of_products

    # Click [element] methods
    def click_on_cancel_button(self):
        self.driver.find_element(*CheckoutPage.cancel_button).click()

    def click_on_finish_button(self):
        self.driver.find_element(*CheckoutPage.finish_button).click()
        checkout_complete_page = CheckoutCompletePage(self.driver)
        return checkout_complete_page

    # Complete action methods

    def checkout_overview_heading_exist(self):
        checkout_overview_heading = self.driver.find_element(*CheckoutPage.title_heading).text
        return True if 'Overview' in checkout_overview_heading else False

    def calculate_item_total(self):
        prices = self.get_price_of_all_items()
        item_total = 0
        for price in prices:
            item_total += float(price)
        return item_total

    def calculate_total(self):
        item_total = self.calculate_item_total()
        tax = self.get_tax()
        return tax+item_total

    def capture_receipt(self, name):
        receipt = self.driver.find_element(*CheckoutPage.receipt_section)
        receipt.screenshot(name)

    def navigate_to_checkout_complete_page(self, plp, cart_page, checkout_form_page, checkout_page):
        plp.click_cart_button()
        cart_page.click_checkout_button()
        checkout_form_page.click_on_continue_button()
        checkout_form_page.enter_first_name("John")
        checkout_form_page.enter_last_name("wick")
        checkout_form_page.enter_post_code("2154")
        checkout_form_page.click_on_continue_button()
        checkout_complete_page = checkout_page.click_on_finish_button()
        return checkout_complete_page
