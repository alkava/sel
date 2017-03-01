# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os.path
import time
from selenium.webdriver.common.keys import Keys


class MainShopPageHelper:

    def __init__(self, app):
        self.app = app

    def select_first_product(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#box-most-popular .product:first-child").click()

    def get_number_of_products(self):
        wd = self.app.wd
        return int(wd.find_element_by_css_selector(".quantity").text)

    def back_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Home").click()


