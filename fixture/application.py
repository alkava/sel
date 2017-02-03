# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.base import BaseHelper
from fixture.admin_page import AdminHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        self.session = SessionHelper(self)
        self.base = BaseHelper(self)
        self.admin_page = AdminHelper(self)
        self.base_url = base_url
        self.browser = browser

    def open_home_page(self, user_side):
        wd = self.wd
        wd.get(self.base_url+user_side)

    def destroy(self):
        self.wd.quit()
