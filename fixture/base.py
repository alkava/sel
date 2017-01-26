from selenium.common.exceptions import NoSuchElementException


class BaseHelper:

    def __init__(self, app):
        self.app = app

    def type(self, locator_type, locator_value, text):
        wd = self.app.wd
        wd.find_element(locator_type, locator_value).click()
        wd.find_element(locator_type, locator_value).clear()
        wd.find_element(locator_type, locator_value).send_keys(text)

    def is_element_presented(self, locator_type, locator_value):
        wd = self.app.wd
        try:
            wd.find_element(locator_type, locator_value)
            return True
        except NoSuchElementException:
            return False
