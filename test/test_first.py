# -*- coding: utf-8 -*-

def test_login(app):

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





