# -*- coding: utf-8 -*-


class Product:

    def __init__(self, status=None, name=None, code=None,
                 categories=None, default_category=None, gender=None, quantity=None, quantity_unit=None,
                 delivery_status=None, sold_out_status=None, image=None, date_from=None, date_to=None,
                 manufacturer=None, supplier=None, keywords=None, short_description=None, description=None,
                 head_title=None, meta_description=None, purchase_price=None, currency=None, tax_class=None,
                 price_incl_tax_usd=None, price_incl_tax_eur=None):
        self.status = status
        self.name = name
        self.code = code
        self.categories = categories
        self.default_category = default_category
        self.gender = gender
        self.quantity = quantity
        self.quantity_unit = quantity_unit
        self.delivery_status = delivery_status
        self.sold_out_status = sold_out_status
        self.image = image
        self.date_from = date_from
        self.date_to = date_to
        self.manufacturer = manufacturer
        self.supplier = supplier
        self.keywords = keywords
        self.short_description = short_description
        self.description = description
        self.head_title = head_title
        self.meta_description = meta_description
        self.purchase_price = purchase_price
        self.currency = currency
        self.tax_class = tax_class
        self.price_incl_tax_usd = price_incl_tax_usd
        self.price_incl_tax_eur = price_incl_tax_eur
