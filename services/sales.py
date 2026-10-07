from models.sale import Sale

class Sales:
    """Calculates the sum total of all sales made"""
    def __init__(self, sales=None):
        self.sales = sales or []

    def record_sale(self, inventory, name, quantity):
        product = inventory.find_product(name)

        if product is None:
            return False
        if quantity > product.quantity:
            return False
        
        product.quantity -= quantity

        total = product.price * quantity

        sale = Sale(
            product.name,
            quantity,
            product.price,
            total
        )

        self.sales.append(sale)

        return True
    
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