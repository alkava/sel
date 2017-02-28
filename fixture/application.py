# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.base import BaseHelper
from fixture.admin_page import AdminHelper
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener



class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value)
    def after_find(self, by, value, driver):
        print(by, value, "found")
    def on_exception(self, exception, driver):
        print(exception)

class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            #self.wd = webdriver.Firefox()
            self.wd = EventFiringWebDriver(webdriver.Firefoxe(), MyListener())
        elif browser == "chrome":
            #self.wd = webdriver.Chrome()
            self.wd = EventFiringWebDriver(webdriver.Chrome(), MyListener())
        elif browser == "ie":
            #self.wd = webdriver.Ie()
            self.wd = EventFiringWebDriver(webdriver.Ie(), MyListener())
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

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
