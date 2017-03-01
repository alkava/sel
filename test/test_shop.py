# -*- coding: utf-8 -*-

import string
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait




def generate_email():
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(random.randrange(5, 20))]) + \
        "@" + ''.join([random.choice(string.ascii_letters) for i in range(random.randrange(5, 10))]) + \
        "." + ''.join([random.choice(string.ascii_letters) for i in range(random.randrange(2, 4))])


def generate_phone():
    return '+' + ''.join([random.choice(string.digits) for i in range(10)])


def test_adding_products_to_the_cart(app, app_shop):
    # Adding products to the shopping cart three times
    for i in range(0, 3):
        app_shop.main_shop_page.select_first_product()
        app_shop.product_page.click_on_add_to_cart_button()
        app_shop.product_page.back_home_page()

    # Opening the Checkout page
    number_of_items = app_shop.checkout_page.open_checkout_page()

    # Removing of items from the shopping cart
    while number_of_items > 0:
        number_of_items = number_of_items - 1
        app_shop.checkout_page.remove_current_product()
        assert app_shop.checkout_page.check_cart_after_product_removing(number_of_items), "Item hasn't been removed."



def test_registration_of_new_user(app, app_shop):
    wd = app.wd

    # initialisation of a customer registration
    wd.find_element_by_link_text("New customers click here").click()

    # filling the form
    app.base.type(By.NAME, "tax_id", "2344")
    app.base.type(By.NAME, "company", "company")
    app.base.type(By.NAME, "firstname", "firstname")
    app.base.type(By.NAME, "lastname", "lastname")
    app.base.type(By.NAME, "address1", "Address 1")
    app.base.type(By.NAME, "address2", "Address 2")
    postcode = ''.join([random.choice(string.digits) for i in range(5)])
    print("postcode: " + postcode)
    app.base.type(By.NAME, "postcode", postcode)
    app.base.type(By.NAME, "city", "New York")
    select = Select(wd.find_element_by_name("country_code"))
    select.select_by_visible_text("United States")

    select = Select(wd.find_element_by_xpath(".//select[@name='zone_code']"))
    WebDriverWait(wd, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, ".//select[@name='zone_code']"), "New York"))
    select.select_by_value("NY")

    email = generate_email()
    print("email: " + email)
    app.base.type(By.NAME, "email", email)
    app.base.type(By.NAME, "phone", generate_phone())
    password = "password"
    print("password: " + password)
    app.base.type(By.NAME, "password", password)
    app.base.type(By.NAME, "confirmed_password", password)

    # Submitting the form
    wd.find_element_by_name("create_account").click()

    wd.find_element_by_link_text("Logout").click()
    app.session.login_to_shop(email, password)
    wd.find_element_by_link_text("Logout").click()


def test_stickers(app, app_shop):
    wd = app.wd
    list_of_all_products_on_the_page = wd.find_elements_by_css_selector(".product")
    count = len(list_of_all_products_on_the_page)
    list_with_failed_products = []
    for el in list_of_all_products_on_the_page:
        title = el.find_element_by_css_selector("a.link").get_attribute("Title")
        print("Check the product: %s" % title)
        if len(el.find_elements_by_css_selector(".stiker")) > 1:
            print("Product %s has more than one sticker." % title)
            list_with_failed_products.append(title)
        else:
            count = count -1
    if count == 0:
        print("All products have one sticker")

    assert count == 0, "Some products have not one sticker: %s" % list_with_failed_products

def test_product_page(app, app_shop):
    wd = app.wd

    # Actions on the Main page

    elements = wd.find_element_by_css_selector("#box-campaigns li.product:nth-child(1)")
    list_of_parameters = [elements.find_element_by_css_selector(".name").text]

    regular_price = elements.find_element_by_css_selector(".regular-price")
    list_of_parameters.append(regular_price.text)

    campaign_price = elements.find_element_by_css_selector(".campaign-price")
    list_of_parameters.append(campaign_price.text)

    r_color = regular_price.value_of_css_property("color") #rgb(119,​ 119,​ 119)
    r_decoration = regular_price.value_of_css_property("text-decoration")  #line-through
    r_font_size = regular_price.value_of_css_property("font-size")

    print(r_color, r_decoration, r_font_size)
    assert ("119, 119, 119" in r_color) and (r_decoration == "line-through"),"Regular price has incorrect style on the Main page"

    c_color = campaign_price.value_of_css_property("color")  # rgb(204, 0, 0)
    c_decoration = campaign_price.get_attribute("localName")  # bold
    c_font_size = campaign_price.value_of_css_property("font-size")
    print(c_color, c_decoration, c_font_size)

    assert "204, 0, 0" in c_color and c_decoration == "strong", "Campaign price has correct style on the Main page"
    assert r_font_size < c_font_size, "Atata! Campaign price should have font size bigger than Regular price"

    # Actions on the page with product details

    elements.click()
    assert wd.find_element_by_css_selector("h1").text == list_of_parameters[0]
    regular_price1 = wd.find_element_by_css_selector("#box-product .regular-price")
    assert regular_price1.text == list_of_parameters[1]
    campaign_price1 = wd.find_element_by_css_selector("#box-product .campaign-price")
    assert campaign_price1.text == list_of_parameters[2]

    r_color1 = regular_price1.value_of_css_property("color")  # rgb(102, 102, 102)
    r_decoration1 = regular_price1.value_of_css_property("text-decoration")  # line-through
    r_font_size1 = regular_price1.value_of_css_property("font-size")
    print(r_color1, r_decoration1, r_font_size1)
    assert "102, 102, 102" in r_color1 and r_decoration1 == "line-through", "Regular price has incorrect style on the Main page"

    c_color1 = campaign_price1.value_of_css_property("color")  # rgb(204, 0, 0)
    c_decoration1 = campaign_price1.get_attribute("localName")  # bold
    c_font_size1 = campaign_price1.value_of_css_property("font-size")
    print(c_color1, c_decoration1, c_font_size1)

    assert "204, 0, 0" in c_color1 and c_decoration1 == "strong", "Campaign price has correct style on the Main page"
    assert r_font_size1 < c_font_size1, "Atata! Campaign price has font size smaller than Regular price"








