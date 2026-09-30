from models.product import Product
from models.sale import Sale
from services.inventory import Inventory
from services.sales import Sales
from storage.file_store import save_products, save_sales, load_products, load_sales


inventory = Inventory()

product_data = load_products("data/products.json")
for data in product_data:
    product = Product(
        data["name"],
        data["price"],
        data["quantity"],
        data["category"]
    )
    inventory.add_product(product)

sales_data = load_sales("data/sales.json")
for data in sales_data:
    sale = Sale(
        data["product_name"],
        data["quantity_sold"],
        data["unit_price"],
        data["total"]
    )
    inventory.sales.append(sale)

def ask_price():
    while True:
            try:
                price = float(input("Enter product price: "))
                if price < 0:
                    print("Price cannot be negative")

                return price
            except ValueError:
                print("Price must be a number")

def ask_quantity():
        while True:
            try:
                quantity = int(input("Enter product quantity: "))
                if quantity < 0:
                    print("Quantity cannot be negative")
                    
                return quantity
            except ValueError:
                print("Quantity must be a whole number")

def add_product(inventory):
        name = input("Enter product name: ")

        if name.strip() == "":
            print("Product cannot be empty")
            return
        
        if inventory.find_product(name):
            print("Product already exists")
            return
        price = ask_price()
        quantity =  ask_quantity()

        
        category = input("Enter a category: ")
        product = Product(name, price, quantity, category)
        inventory.add_product(product)
        
        print("Product added successfully")

def list_product(inventory):
    print("\n| Name   | Price   | Quantity   | Category   |")
    
    total_stock_value = 0
    
    for product in inventory.list_product():
        print(
            f"| {product.name:<10}"
            f"| {product.price:<10,.2f}"
            f"| {product.quantity:<10}"
            f"| {product.category} |"
            )
    
        total_stock_value += product.price * product.quantity
    
    print(f"Total stock value: {total_stock_value:,.2f}")

def find_product(inventory):
    search = input("Enter product name: ").lower()
    
    found = False
    
    for product in inventory.list_product():
        if search in product.name.lower():
            print(product.show())
            found = True
    
    if not found:
        print("Product not found")


def update_stock(inventory):
    name = input("Enter product name: ")
    product = inventory.find_product(name)
    
    if product is None:
        print("Product not found")
        return
    
    try:
        quantity = int(input("Enter new quantity: "))
    except ValueError:
        print("Quantity must be whole number")
        return

    
    if quantity < 0:
        print("Quantity cannot be negative")
        return
    
    
    inventory.update_quantity(name, quantity)
    print("Stock quantity updated successfully")


def record_sale(inventory):
    name = input("Enter product name: ")
    
    product = inventory.find_product(name)
    
    if product is None:
        print("Product not found")
        return


    try:
        quantity = int(input("Enter quantity sold: "))
    except ValueError:
        print("Quantity must be a whole number")
        return
    
    if quantity <= 0:
        print("Quantity must be greater than 0")
        return
    
    if product.quantity < quantity:
        print("Insufficient stock")
        return
    
    inventory.record_sale(name, quantity)
    print("Sale recorded successfully")


def low_stock_report(inventory):
    low_products = inventory.low_stock()
    
    if not low_products:
        print("No products are low in stock")
    
    else:
        print("\n ---- LOW STOCK ----")
    
        for product in low_products:
            print(product.show())

def sales_report(inventory):
    sales = Sales(inventory.sales)
    
    
    print("\n ---- SALES REPORT ----")
    print(f"Total number of sales: {len(inventory.sales)}")
    print(f"Total money made: {sales.total_value()}")
    
    best_product = sales.best_selling_product()
    
    if best_product is None:
        print("Best selling product: No sales yet")
    else:
        print(f"Best selling product: {best_product}")



def show_menu():
    print("\n---- SHOP INVENTORY ----")
    print("1 Add a product")
    print("2 List all products")
    print("3 Find a product")
    print("4 Update stock quantity")
    print("5 Record a sale")
    print("6 Low stock report")
    print("7 Sales report")
    print("8 Quit")


actions = {
    "1": lambda: add_product(inventory),
    "2": lambda: list_product(inventory),
    "3": lambda: find_product(inventory),
    "4": lambda: update_stock(inventory),
    "5": lambda: record_sale(inventory),
    "6": lambda: low_stock_report(inventory),
    "7": lambda: sales_report(inventory),
}

while True:
    show_menu()

    choice = input("Choose an option: ")


    if choice == "8":
        save_products(inventory.products)
        save_sales(inventory.sales)
        print("Save to file")
        break


    action = actions.get(choice)

    if action:action()
    else:
        print("Invalid choice")