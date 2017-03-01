# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os.path
from fixture.main_shop_page import MainShopPageHelper
import time
from selenium.webdriver.common.keys import Keys


class ProductHelper(MainShopPageHelper):

    def __init__(self, app):
        self.app = app

    def click_on_add_to_cart_button(self):
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        quantity_items_before = self.get_number_of_products()
        print("quantity_items_before  " + str(quantity_items_before))
        wd.find_element_by_name("add_cart_product").click()
        wait.until(lambda x: (int(x.find_element_by_css_selector(".quantity").text)) == quantity_items_before + 1)
