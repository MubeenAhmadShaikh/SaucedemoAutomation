from selenium.webdriver.common.by import By
from pageObjects.Page import Page
from selenium.common.exceptions import NoSuchElementException


class ProductsListPage(Page):

    # def __init__(self, driver):
    #     self.driver = driver

    cart_buttons = (By.XPATH, "//div[@class='pricebar']/button")
    remove_buttons = (By.XPATH, "//div[@class='pricebar']/button[text()='Remove']")
    cart_icons = (By.CSS_SELECTOR, "span[class='shopping_cart_badge']")
    cart_icon_button = (By.CSS_SELECTOR, ".shopping_cart_link")
    price_tags = (By.CSS_SELECTOR, "div[class='inventory_item_price']")
    hamburger_menu = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    product_locator = (By.CSS_SELECTOR, ".inventory_item")
    product_name_locator = (By.CSS_SELECTOR, ".inventory_item_name")
    product_price_locator = (By.CSS_SELECTOR, ".inventory_item_price")
    page_heading = (By.CSS_SELECTOR, ".title")
    filter_dropdown = (By.CSS_SELECTOR, "select[class='product_sort_container']")

    def sort_products_a_to_z(self):
        sort_menu_locator = self.driver.find_element(*ProductsListPage.filter_dropdown)
        self.selectOptionByText(sort_menu_locator, "Name (A to Z)")

    def sort_products_z_to_a(self):
        sort_menu_locator = self.driver.find_element(*ProductsListPage.filter_dropdown)
        self.selectOptionByText(sort_menu_locator, "Name (Z to A)")

    def sort_products_low_to_high(self):
        sort_menu_locator = self.driver.find_element(*ProductsListPage.filter_dropdown)
        self.selectOptionByText(sort_menu_locator, "Price (low to high)")

    def sort_products_high_to_low(self):
        sort_menu_locator = self.driver.find_element(*ProductsListPage.filter_dropdown)
        self.selectOptionByText(sort_menu_locator, "Price (high to low)")

    def add_all_products_to_cart(self):
        add_to_cart_buttons = self.get_add_to_cart_buttons()
        remove_buttons = self.get_all_remove_buttons()
        if add_to_cart_buttons:
            for button in add_to_cart_buttons:
                button.click()
        elif remove_buttons:
            self.empty_cart()
        else:
            print("No Products are available")
    def get_all_products(self):
        products = self.driver.find_elements(*ProductsListPage.product_locator)
        return products

    def get_all_products_name(self):
        product_names = self.driver.find_elements(*ProductsListPage.product_name_locator)
        return product_names

    def get_all_product_prices(self):
        product_prices = self.driver.find_elements(*ProductsListPage.product_price_locator)
        return product_prices

    def get_add_to_cart_buttons(self):
        return self.driver.find_elements(*ProductsListPage.cart_buttons)

    def get_page_heading(self):
        heading_text = self.driver.find_element(*ProductsListPage.page_heading).text
        return heading_text

    def get_number_of_cart_items(self):
        try:
            cart_items = self.driver.find_element(*ProductsListPage.cart_icons).text
            return int(cart_items) if cart_items else 0
        except NoSuchElementException:
            return 0


    def click_hamburger_menu(self):
        hamburger_menu = self.driver.find_element(*ProductsListPage.hamburger_menu)
        hamburger_menu.click()

    def click_sort_menu(self):
        sort_products_menu = self.driver.find_element(*ProductsListPage.filter_dropdown)
        sort_products_menu.click()

    def get_sort_menu(self):
        return self.driver.find_element(*ProductsListPage.filter_dropdown)

    def click_cart_button(self):
        cart_button = self.driver.find_element(*ProductsListPage.cart_icon_button)
        cart_button.click()

    def get_all_remove_buttons(self):
        return self.driver.find_elements(*ProductsListPage.remove_buttons)

    def add_to_cart_product_by_title(self, title):
        id_title = '-'.join(title.lower().split(' '))
        cart_btn_selectors = (By.CSS_SELECTOR, "button[name='add-to-cart-" + id_title + "']")
        cart_buttons = self.driver.find_elements(*cart_btn_selectors)
        for add_to_cart in cart_buttons:
            add_to_cart.click()
        return cart_buttons

    def add_to_cart_product_by_price(self, price):
        cart_btn_selectors = (By.XPATH, "//div[@class='inventory_item_price'][text()='" + price + "']/../button")
        cart_buttons = self.driver.find_elements(*cart_btn_selectors)
        for add_to_cart in cart_buttons:
            add_to_cart.click()

        return cart_buttons

    def get_list_of_products_by_price(self, price):
        product_containers = self.driver.find_elements(*ProductsListPage.product_locator)
        products = []
        for product in product_containers:
            product_price = product.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
            if product_price[1:] == price:
                products.append(product)
        return products

    def get_list_of_products_by_title(self, title):
        product_containers = self.driver.find_elements(*ProductsListPage.product_locator)
        products = []
        for product in product_containers:
            product_title = product.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
            if product_title == title:
                products.append(product)
        return products

    def empty_cart(self):
        remove_buttons = self.get_all_remove_buttons()
        if remove_buttons:
            for button in remove_buttons:
                button.click()




