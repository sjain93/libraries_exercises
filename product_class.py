class Product:
    """ A class representing a Product to be added to the shopping cart"""

    def __init__(self, name, base_price, tax):
        self.name = str(name)
        self.base_price = float(base_price)
        self.tax= float(tax)
