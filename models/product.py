class Product:
    """ A single product in the shop."""
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category
        }

    def total_value(self):
        """Return what the product is worth."""
        return self.price * self.quantity
    
    def is_low(self):
        """Return True if there are product with fewer unit than 5."""
        if self.quantity < 5:
            return True
        else:
            return False

    def show(self):
        return f"{self.name} - {self.price} - {self.quantity} - {self.category}"