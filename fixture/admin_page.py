# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminHelper:

    def __init__(self, app):
        self.app = app


    def is_element_presented(self, locator):
        wd = self.app.wd
        try:
            element = WebDriverWait(wd, 10).until(
                EC.presence_of_element_located(locator)
            )
            # print("Element has been found")
            return True
        except Exception:
            print("Element hasn't been found")
            return False

    # Menu Appearence
    def open_appearence_menu(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath("//li[@id='app-'][.//a[contains(@href, 'app=appearance')]]")
        if element.get_attribute("class") != 'selected':
            element.click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_template_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-template>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_logotype_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-logotype>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    # Menu Catalog
    def open_catalog_menu(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath("//li[@id='app-'][.//a[contains(@href, 'app=catalog')]]")
        if element.get_attribute("class") != 'selected':
            element.click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_catalog_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-catalog>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_product_groups_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-product_groups>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_option_groups_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-option_groups>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_manufacturers_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-manufacturers>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_suppliers_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-suppliers>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_delivery_statuses_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-delivery_statuses>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_sold_out_statuses_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-sold_out_statuses>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_quantity_units_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-quantity_units>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_csv_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-csv>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    # Menu Countries
    def open_countries_menu(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath("//li[@id='app-'][.//a[contains(@href, 'app=countries')]]")
        if element.get_attribute("class") != 'selected':
            element.click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    # Menu Currencies
    def open_currencies_menu(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath("//li[@id='app-'][.//a[contains(@href, 'app=currencies')]]")
        if element.get_attribute("class") != 'selected':
            element.click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    # Menu Customers
    def open_customers_menu(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath("//li[@id='app-'][.//a[contains(@href, 'app=customers')]]")
        if element.get_attribute("class") != 'selected':
            element.click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_customers_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-customers>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_customers_csv_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-csv>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_newsletter_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-newsletter>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    # Menu Geo Zones
    def open_geo_zones_menu(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath("//li[@id='app-'][.//a[contains(@href, 'app=geo_zones')]]")
        if element.get_attribute("class") != 'selected':
            element.click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    # Menu Languages
    def open_languages_menu(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath("//li[@id='app-'][.//a[contains(@href, 'app=languages')]]")
        if element.get_attribute("class") != 'selected':
            element.click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_languages_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-languages>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_storage_encoding_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-storage_encoding>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    # Menu Modules
    def open_modules_menu(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath("//li[@id='app-'][.//a[contains(@href, 'app=modules')]]")
        if element.get_attribute("class") != 'selected':
            element.click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_jobs_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-jobs>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_modules_customer_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-customer>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_shipping_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-shipping>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_payment_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-payment>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_storage_order_total(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-order_total>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_order_success_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-order_success>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_order_action_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-order_action>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    # Menu Orders

    def open_orders_menu(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath("//li[@id='app-'][.//a[contains(@href, 'app=orders')]]")
        if element.get_attribute("class") != 'selected':
            element.click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_orders_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-orders>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_order_statuses_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-order_statuses>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    # Menu Pages

    def open_pages_menu(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath("//li[@id='app-'][.//a[contains(@href, 'app=pages')]]")
        if element.get_attribute("class") != 'selected':
            element.click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    # Menu Reports
    def open_reports_menu(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath("//li[@id='app-'][.//a[contains(@href, 'app=reports')]]")
        if element.get_attribute("class") != 'selected':
            element.click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_monthly_sales_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-monthly_sales>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_most_sold_products_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-most_sold_products>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_most_shopping_customers_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-most_shopping_customers>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    # Menu Settings
    def open_settings_menu(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath("//li[@id='app-'][.//a[contains(@href, 'app=settings')]]")
        if element.get_attribute("class") != 'selected':
            element.click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_store_info_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-store_info>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_defaults_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-defaults>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_general_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-general>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_listings_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-listings>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_checkout_total(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-checkout>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_advanced_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-advanced>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_images_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-images>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_security_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-security>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    # Menu Slides
    def open_slides_menu(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath("//li[@id='app-'][.//a[contains(@href, 'app=slides')]]")
        if element.get_attribute("class") != 'selected':
            element.click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    # Menu Tax
    def open_tax_menu(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath("//li[@id='app-'][.//a[contains(@href, 'app=tax')]]")
        if element.get_attribute("class") != 'selected':
            element.click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_tax_classes_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-tax_classes>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_tax_rates_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-tax_rates>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    # Menu Translations
    def open_translations_menu(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath("//li[@id='app-'][.//a[contains(@href, 'app=translations')]]")
        if element.get_attribute("class") != 'selected':
            element.click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_search_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-search>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_scan_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-scan>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_translations_csv_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-csv>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    # Menu Users
    def open_users_menu(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath("//li[@id='app-'][.//a[contains(@href, 'app=users')]]")
        if element.get_attribute("class") != 'selected':
            element.click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    # Menu vQmods

    def open_vqmods_menu(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath("//li[@id='app-'][.//a[contains(@href, 'app=vqmods')]]")
        if element.get_attribute("class") != 'selected':
            element.click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

    def open_vqmods_submenu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#doc-vqmods>a").click()
        self.is_element_presented((By.CSS_SELECTOR, "h1"))

