# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

def test_menu(app, app_admin):
    wd = app.wd
    xpath_selector = "//li[@id='app-']"
    number_of_menu_items = len(wd.find_elements_by_xpath(xpath_selector))
    list_of_failed_items = []
    counter = 0
    i = 1
    while i <= number_of_menu_items:
        menu_item = wd.find_element_by_xpath(xpath_selector+"["+str(i)+"]")
        menu_item.click()

        number_of_submenu_items = len(wd.find_elements_by_xpath(xpath_selector+" //li"))
        if number_of_submenu_items != 0:
            j = 1
            while j <= number_of_submenu_items:
                submenu_item = wd.find_element_by_xpath(xpath_selector + " //li[" + str(j) + "]")
                submenu_item.click()
                if not app.admin_page.is_element_presented((By.CSS_SELECTOR, "h1")):
                    counter = counter + 1
                    list_of_failed_items.append("Sub-menu item: %s" % wd.find_element_by_xpath(xpath_selector + " //li[" + str(j) + "]").text)
                j = j + 1

        else:
            if not app.admin_page.is_element_presented((By.CSS_SELECTOR, "h1")):
                counter = counter + 1
                list_of_failed_items.append(
                    "Menu item: %s" % wd.find_element_by_xpath(xpath_selector+"["+str(i)+"]").text)
        j = 0
        i = i + 1

    assert counter == 0, str(counter) + " item(s) has(have) no element 'h1' \n %s" % list_of_failed_items

def test_sorting_of_countries(app, app_admin):
    wd = app.wd
    app.admin_page.open_countries_menu()
    countries_column = wd.find_elements_by_css_selector(".row td:nth-of-type(5)")
    list_of_countries = [x.text for x in countries_column]
    sorted_list = sorted(list_of_countries)
    assert sorted_list == list_of_countries, "List is not sorted"

def test_sorting_of_zones_per_countries(app, app_admin):
    wd = app.wd
    app.admin_page.open_countries_menu()
    rows = [x.text for x in wd.find_elements_by_xpath(".//*[@class='row'] [.//td[6]!=0]//td[5]")]
    print(rows)
    count = len(rows)
    for el in rows:
        wd.find_element_by_link_text(el).click()
        zones_column = wd.find_elements_by_xpath(".//*[@id='table-zones']//tr[position() < last()]/td[3]")

        list_of_zones = [x.text for x in zones_column]
        sorted_list = sorted(list_of_zones)
        if sorted_list == list_of_zones:
            print("List of Zones for " + el + " is sorted")
            count = count -1
        else:
            print("List of Zones for " + el + " is not sorted")
        wd.execute_script("window.history.go(-1)")

    assert count == 0, "Some countries have unsorted list of Zones. Look at output above"

def test_login(app, app_admin):
    # Menu Appearence

    app.admin_page.open_appearence_menu()

    app.admin_page.open_template_submenu()
    app.admin_page.open_logotype_submenu()
    # Menu Catalog
    app.admin_page.open_catalog_menu()
    app.admin_page.open_catalog_submenu()
    app.admin_page.open_product_groups_submenu()
    app.admin_page.open_option_groups_submenu()
    app.admin_page.open_manufacturers_submenu()
    app.admin_page.open_suppliers_submenu()
    app.admin_page.open_delivery_statuses_submenu()
    app.admin_page.open_sold_out_statuses_submenu()
    app.admin_page.open_quantity_units_submenu()
    app.admin_page.open_csv_submenu()
    # Menu Countries
    app.admin_page.open_countries_menu()
    # Menu Currencies
    app.admin_page.open_currencies_menu()
    # Menu Customers
    app.admin_page.open_customers_menu()
    app.admin_page.open_customers_submenu()
    app.admin_page.open_customers_csv_submenu()
    app.admin_page.open_newsletter_submenu()
    # Menu Geo Zones
    app.admin_page.open_geo_zones_menu()
    # Menu Languages
    app.admin_page.open_languages_menu()
    app.admin_page.open_languages_submenu()
    app.admin_page.open_storage_encoding_submenu()
    # Menu Modules
    app.admin_page.open_modules_menu()
    app.admin_page.open_jobs_submenu()
    app.admin_page.open_modules_customer_submenu()
    app.admin_page.open_shipping_submenu()
    app.admin_page.open_payment_submenu()
    app.admin_page.open_storage_order_total()
    app.admin_page.open_order_success_submenu()
    app.admin_page.open_order_action_submenu()
    # Menu Orders
    app.admin_page.open_orders_menu()
    app.admin_page.open_orders_submenu()
    app.admin_page.open_order_statuses_submenu()
    # Menu Pages
    app.admin_page.open_pages_menu()
    # Menu Reports
    app.admin_page.open_reports_menu()
    app.admin_page.open_monthly_sales_submenu()
    app.admin_page.open_most_sold_products_submenu()
    app.admin_page.open_most_shopping_customers_submenu()
    # Menu Settings
    app.admin_page.open_settings_menu()
    app.admin_page.open_store_info_submenu()
    app.admin_page.open_defaults_submenu()
    app.admin_page.open_general_submenu()
    app.admin_page.open_listings_submenu()
    app.admin_page.open_checkout_total()
    app.admin_page.open_advanced_submenu()
    app.admin_page.open_images_submenu()
    app.admin_page.open_security_submenu()

    # Menu Slides
    app.admin_page.open_slides_menu()

    # Menu Tax
    app.admin_page.open_tax_menu()
    app.admin_page.open_tax_classes_submenu()
    app.admin_page.open_tax_rates_submenu()

    # Menu Translations
    app.admin_page.open_translations_menu()
    app.admin_page.open_search_submenu()
    app.admin_page.open_scan_submenu()
    app.admin_page.open_translations_csv_submenu()

    # Menu Users
    app.admin_page.open_users_menu()

    # Menu vQmods

    app.admin_page.open_vqmods_menu()
    app.admin_page.open_vqmods_submenu()





