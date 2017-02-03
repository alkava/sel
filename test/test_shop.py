# -*- coding: utf-8 -*-

def test_stickers(app, app_shop):
    wd = app.wd
    list_of_all_products_on_the_page = wd.find_elements_by_css_selector(".product")
    count = len(list_of_all_products_on_the_page)
    for el in list_of_all_products_on_the_page:
        print("Check the product: %s" % el.find_element_by_css_selector("a.link").get_attribute("Title"))
        if len(el.find_elements_by_css_selector(".stiker")) > 1:
            print("Product %s has more than one sticker." % el.find_element_by_css_selector("a.link").get_attribute("Title"))
        else:
            count = count -1
    if count == 0:
        print("All products have one sticker")





