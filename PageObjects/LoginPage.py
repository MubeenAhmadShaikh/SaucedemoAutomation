from selenium.webdriver.common.by import By
from PageObjects.Page import Page


class LoginPage(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.init_site()

    username_field = (By.CSS_SELECTOR, "input[id='user-name']")
    password_field = (By.CSS_SELECTOR, "input[id='password']")
    login_button = (By.CSS_SELECTOR, "input[id='login-button']")
    error_message = (By.CLASS_NAME, "error-message-container")
    error = (By.TAG_NAME, "h3")
    title = (By.CLASS_NAME, "title")

    def get_user_name_field(self):
        return self.driver.find_element(*LoginPage.username_field)

    def get_password_field(self):
        return self.driver.find_element(*LoginPage.password_field)

    def get_login_button(self):
        return self.driver.find_element(*LoginPage.login_button)

    def enter_username(self, username):
        """ Enter username. """
        self.driver.find_element(*LoginPage.username_field).send_keys(username)

    def enter_password(self, password):
        """ Enter password. """
        self.driver.find_element(*LoginPage.password_field).send_keys(password)

    def click_login(self):
        """ Click on login button. """
        self.driver.find_element(*LoginPage.login_button).click()

    def get_error_message_text(self):
        """ Returns the error message on the page if exists, else returns None. """
        return self.driver.find_element(*LoginPage.error_message).text.split(':')[1]

    def error_message_exist(self):
        """ Returns True if error message exists on the page else False. """
        return True if self.driver.find_element(*LoginPage.error_message) else False

    def perform_complete_login(self):
        """ Performs complete end to end login with valid credentials. """
        pass

    def title_exists(self):
        """ Returns True if the title exists after successful login else false"""
        return True if "Products" in self.driver.find_element(*LoginPage.title).text else False
