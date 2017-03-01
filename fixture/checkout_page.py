# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fixture.main_shop_page import MainShopPageHelper
import os.path
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class CheckoutHelper(MainShopPageHelper):

    def __init__(self, app):
        self.app = app

    def open_checkout_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Checkout »").click()
        wd.find_element_by_class_name("viewport").click()
        return self.get_number_of_products_on_the_checkout_page()

    def get_number_of_products_on_the_checkout_page(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector(".dataTable td.item"))

    def remove_current_product(self):
        wd = self.app.wd

        wd.find_element_by_name("remove_cart_item").click()

    def check_cart_after_product_removing(self, number_of_items):
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        try:
            if number_of_items != 0:
                value = wait.until(
                    lambda x: (self.get_number_of_products_on_the_checkout_page()) == number_of_items)
                return value
            else:
                value = wait.until(
                    EC.text_to_be_present_in_element((By.ID, "checkout-cart-wrapper"), "There are no items in your cart."))
                return value
        except TimeoutException:
            return False

