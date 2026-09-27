class Sales:
    """Calculates the sum total of all sales made"""
    def __init__(self, sales):
        self.sales = sales

    def total_value(self):
        total = 0

        for sale in self.sales:
            total += sale.total

        return total

    def best_selling_product(self):
        highest_quantity = 0
        best_product = None

        for sale in self.sales:
            if sale.quantity_sold > highest_quantity:
                highest_quantity = sale.quantity_sold
                best_product = sale.product_name

        return best_product
