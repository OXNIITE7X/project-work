from models.sale import Sale

class Inventory:
    """Products in the shop"""
    def __init__(self, products=None, sales=None):
        self.products = products or []
        self.sales = sales or []

    def add_product(self, product):
        """Return the products added"""
        self.products.append(product)

    def find_product(self,name):
        """Return the product if found"""
        for product in self.products:
            if product.name == name:
                return product

    def list_product(self):
        """Return the list of products"""
        return self.products

    def update_quantity(self, name, quantity):
        """Return the updated quantity of product"""
        product = self.find_product(name)
        product.quantity = quantity

    def low_stock(self):
        """Return products that are low on stock"""
        low_products = []

        for product in self.products:
            if product.is_low():
                low_products.append(product)

        return low_products

    def record_sale(self, name, quantity):
        product = self.find_product(name)

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