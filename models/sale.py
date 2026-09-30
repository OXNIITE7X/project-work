class Sale:
    """A record of one products sale"""
    def __init__(self, product_name, quantity_sold, unit_price, total):
        self.product_name = product_name
        self.quantity_sold = quantity_sold
        self.unit_price = unit_price
        self.total = total

    def to_dict(self):
        return {
            "product_name": self.product_name,
            "quantity_sold": self.quantity_sold,
            "unit_price": self.unit_price,
            "total": self.total
        }
