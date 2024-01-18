from selenium.webdriver.common.by import By
from PageObjects.Page import Page


class CheckoutCompletePage(Page):

    title_text = (By.CSS_SELECTOR, ".title")
    message = (By.CSS_SELECTOR, ".complete-header")
    back_button = (By.CSS_SELECTOR, "button[name='back-to-products']")

    def get_title(self):
        return self.driver.find_element(*CheckoutCompletePage.title_text).text

    def get_success_message(self):
        return self.driver.find_element(*CheckoutCompletePage.message).text

    def click_on_back_button(self):
        return self.driver.find_element(*CheckoutCompletePage.back_button).click()
