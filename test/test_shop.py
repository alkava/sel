# -*- coding: utf-8 -*-

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





