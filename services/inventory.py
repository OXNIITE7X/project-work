from models.sale import Sale

class Inventory:
    def __init__(self):
        self.products = []
        self.sales = []

    def add_product(self, product):
        self.products.append(product)

    def find_product(self,name):
        for product in self.products:
            if product.name == name:
                return product

    def list_product(self):
        return self.products

    def update_quantity(self, name, quantity):
        product = self.find_product(name)
        product.quantity = quantity

    def low_stock(self):
        low_products = []

        for product in self.products:
            if product.is_low():
                low_products.append(product)

        return low_products

    def record_sale(self, name, quantity):
        product = self.find_product(name)

        if product.quantity < quantity:
            return "Insufficient stock"
        else:
            product.quantity -= quantity

            sale = Sale(
                product.name,
                quantity,
                product.price,
                quantity * product.price
            )

            self.sales.append(sale)