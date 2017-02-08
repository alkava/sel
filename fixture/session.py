# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import config


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login_to_admin_part(self, username, password):
        wd = self.app.wd
        self.app.open_home_page(config.admin_page)

        self.app.base.type(By.NAME, "username", username)
        self.app.base.type(By.NAME, "password", password)
        wd.find_element_by_name('login').click()
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.fa.fa-sign-out.fa-lg')))

    def login_to_shop(self, email, password):
        wd = self.app.wd
        self.app.open_home_page(config.shop_main_page)

        self.app.base.type(By.NAME, "email", email)
        self.app.base.type(By.NAME, "password", password)
        wd.find_element_by_name('login').click()
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Logout')))

    def is_logged_in(self):
        wd = self.app.wd
        return self.app.base.is_element_presented(By.CSS_SELECTOR, '.fa.fa-sign-out.fa-lg')

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def logout(self):
        wd = self.app.wd
        element = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.fa.fa-sign-out.fa-lg')))
        element.click()

