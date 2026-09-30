import json
import os

def _write_json(path, rows):
    os.makedirs("data", exist_ok=True)
    with open(path, "w") as file:
        json.dump(rows, file, indent=2)

def save_products(products):
    """Save the products to a file"""
    _write_json("data/products.json", [product.to_dict() for product in products])

def load_products(filename):
    """Load the product data from file"""
    try:
        with open(filename, "r") as file:
            data = json.load(file)


        return data

    except FileNotFoundError:
        return[]

def save_sales(sales):
    """Return the saved file"""
    _write_json("data/sales.json", [sale.to_dict() for sale in sales])


def load_sales(filename):
    """Load the sales product"""
    try:
        with open(filename, "r") as file:
            data = json.load(file)


        return data

    except FileNotFoundError:
        return []