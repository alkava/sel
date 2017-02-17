# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os.path
import time
from selenium.webdriver.common.keys import Keys

class AdminHelper:

    def __init__(self, app):
        self.app = app

    def is_element_presented(self, locator) -> object:
        wd = self.app.wd
        try:
            WebDriverWait(wd, 2).until(EC.presence_of_element_located(locator))
            # print("Element has been found")
            return True
        except Exception:
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

    # New product

    def add_new_product(self, product):
        wd = self.app.wd
        self.init_adding_new_product()
        self.fill_general_tab(product)
        self.fill_information_tab(product)
        self.fill_prices_tab(product)
        wd.find_element_by_name("save").click()

    def init_adding_new_product(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Add New Product").click()

    def fill_general_tab(self, product):
        wd = self.app.wd
        wd.find_element_by_link_text("General").click()
        wd.find_element_by_xpath(".//*[@name='status'][@value="+product.status+"]").click()
        self.app.base.type(By.NAME, "name[en]", product.name)
        self.app.base.type(By.NAME, "code", product.code)

        elements = wd.find_elements_by_css_selector("input[name='categories[]']")
        for el in elements:
            if el.is_selected():
                el.click()

        wd.find_element_by_xpath(".//*[@data-name='"+product.categories+"']").click()

        select = Select(wd.find_element_by_name("default_category_id"))
        select.select_by_visible_text(product.default_category)

        elements = wd.find_elements_by_css_selector("input[name='product_groups[]']")
        for el in elements:
            if el.is_selected():
                el.click()

        wd.find_element_by_xpath(".//td[contains(text(),'"+product.gender+"')]/..//input").click()
        self.app.base.type(By.NAME, "quantity", product.quantity)
        wd.find_element_by_tag_name("body").click()

        select = Select(wd.find_element_by_name("quantity_unit_id"))
        select.select_by_visible_text(product.quantity_unit)

        select = Select(wd.find_element_by_name("delivery_status_id"))
        select.select_by_visible_text(product.delivery_status)

        select = Select(wd.find_element_by_name("sold_out_status_id"))
        select.select_by_visible_text(product.sold_out_status)

        string = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), product.image)

        print("Path of the imge: " + string)
        wd.find_element_by_name("new_images[]").send_keys(string)
        #wd.find_element_by_name("date_valid_from").send_keys(Keys.HOME + product.date_from)

        self.set_date_picker("date_valid_from", product.date_from)
        #wd.find_element_by_name("date_valid_to").send_keys(Keys.HOME + product.date_to)
        self.set_date_picker("date_valid_to", product.date_to)

    def set_date_picker(self, selector, date):
        wd = self.app.wd
        wd.execute_script(
            'document.querySelector("[name='+selector+']").removeAttribute("type")')
        self.app.base.type(By.NAME, selector, date)

    def fill_information_tab(self, product):
        wd = self.app.wd
        wd.find_element_by_link_text("Information").click()
        WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'trumbowyg-editor')))
        select = Select(wd.find_element_by_name("manufacturer_id"))
        select.select_by_visible_text(product.manufacturer)
        if product.supplier != None:
            select = Select(wd.find_element_by_name("supplier_id"))
            select.select_by_visible_text(product.manufacturer)
        self.app.base.type(By.NAME, "keywords", product.keywords)
        self.app.base.type(By.NAME, "short_description[en]", product.short_description)


        element = wd.find_element_by_css_selector(".input-wrapper[style='white-space: normal;']")
        element.click()
        element.find_element_by_name("description[en]").send_keys("Some Sample Text Here")



        self.app.base.type(By.NAME, "head_title[en]", product.head_title)
        self.app.base.type(By.NAME, "meta_description[en]", product.meta_description)

    def fill_prices_tab(self, product):
        wd = self.app.wd
        wd.find_element_by_link_text("Prices").click()
        WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.ID, 'add-campaign')))
        self.app.base.type(By.NAME, "purchase_price", product.purchase_price)
        select = Select(wd.find_element_by_name("purchase_price_currency_code"))
        select.select_by_visible_text(product.currency)
        if product.tax_class != None:
            select = Select(wd.find_element_by_name("tax_class_id"))
            select.select_by_visible_text(product.tax_class)
        self.app.base.type(By.NAME, "gross_prices[USD]", product.price_incl_tax_usd)
        self.app.base.type(By.NAME, "gross_prices[EUR]", product.price_incl_tax_eur)



