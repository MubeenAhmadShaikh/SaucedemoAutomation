from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckoutPage


class CheckoutFormPage:

    def __init__(self, driver):
        self.driver = driver

    # Checkout Form page element locators
    title_text = (By.CSS_SELECTOR, ".title")
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    post_code = (By.ID, "postal-code")
    cancel_button = (By.ID, "cancel")
    continue_button = (By.ID, "continue")
    error_message = (By.CSS_SELECTOR, ".error-message-container h3")

    # get [element] methods
    def get_information_page_heading(self):
        return self.driver.find_element(*CheckoutFormPage.title_text).text

    def get_first_name(self):
        return self.driver.find_element(*CheckoutFormPage.first_name).get_attribute("value")

    def get_last_name(self):
        return self.driver.find_element(*CheckoutFormPage.last_name).get_attribute("value")

    def get_post_code(self):
        return self.driver.find_element(*CheckoutFormPage.post_code).get_attribute("value")

    def get_error_message(self):
        return self.driver.find_element(*CheckoutFormPage.error_message).text

    def get_continue_button(self):
        self.driver.find_element(*CheckoutFormPage.continue_button).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page

    # Click [element] methods
    def click_on_cancel_button(self):
        cancel_button = self.driver.find_element(*CheckoutFormPage.cancel_button)
        if cancel_button:
            cancel_button.click()
        else:
            print("Cancel button on information page is not available")

    def click_on_continue_button(self):
        self.driver.find_element(*CheckoutFormPage.continue_button).click()

    # Enter [data]
    def enter_first_name(self, first_name):
        self.driver.find_element(*CheckoutFormPage.first_name).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*CheckoutFormPage.last_name).send_keys(last_name)

    def enter_post_code(self, post_code):
        self.driver.find_element(*CheckoutFormPage.post_code).send_keys(post_code)

    def error_exist(self):
        return True if self.get_error_message() else False

    def information_page_heading_exist(self):
        heading_text = self.driver.find_element(*CheckoutFormPage.title_text).text
        return True if 'Information' in heading_text else False

    # Complete action methods
    def navigate_to_checkout_overview_page(self, plp, cart_page, checkout_form_page):
        plp.click_cart_button()
        cart_page.click_checkout_button()
        checkout_form_page.click_on_continue_button()
        checkout_form_page.enter_first_name("John")
        checkout_form_page.enter_last_name("wick")
        checkout_form_page.enter_post_code("2154")
        checkout_form_page.click_on_continue_button()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page
