import json

def save_products(products, filename):
    """Save the products to a file"""
    data = []


    for product in products:
        data.append({
            "name": product.name,
            "price": product.price,
            "quantity": product.quantity,
            "category": product.category
        })

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_products(filename):
    """Load the product data from file"""
    try:
        with open(filename, "r") as file:
            data = json.load(file)


        return data

    except FileNotFoundError:
        return[]

def save_sales(sales, filename):
    """Return the saved file"""
    data = []

    for sale in sales:
        data.append({
            "product_name": sale.product_name,
            "quantity_sold": sale.quantity_sold,
            "unit_price": sale.unit_price,
            "total": sale.total
        })

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_sales(filename):
    """Load the sales product"""
    try:
        with open(filename, "r") as file:
            data = json.load(file)


        return data

    except FileNotFoundError:
        return []