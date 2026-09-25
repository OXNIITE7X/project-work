class Inventory:
    def __init__(self):
        self.products = []

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

# rice = -Poduct("Rice", 4000, 4, "Food")


# inventory = Inventory()
# Inventory.add_product(Rice)
# print(Inventory())
# print(Inventory.add_product(beans))
# print(Inventory.add_product(bread))
# print(Inventory.add_product(milk))