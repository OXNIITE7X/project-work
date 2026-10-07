## SHOP INVENTORY AND SALES SYSTEM
The inventory app is a console app for a small shop. It keeps a list of products, track how much stock there is, records sales, reduces stock when something is sold and saves everything to a file so data can always be used.
        
### HOW TO RUN IT
```
git clone https://github.com/OXNIITE7X/project-work.git
```
- cd project-work
- cd inventory-app
- python main.py

## PROJECT WORK
- *main.py:* The menu loop, and nothing else.
- *models/product.py:* The Product class
- *models/sale.py:* The Sale class
- *services/inventory.py:* Adding, finding, updating products
- *services/sales.py:* Recording sales, sales reports
- *storage/file_store.py:* Saving to and loading from JSON
- *data/products.json:* stores the saved products in the inventory
- *data/sales.json:* Stores the recorded sales

## ---- SHOP INVENTORY ----
1. Add a product
2. List all products
3. Find a product
4. Update stock quantity
5. Record a sale
6. Low stock report
7. Sales report
8. Quit

#### choose an option: 1
- Enter product name: Akara
- Enter product price: 5000
- Enter product quantity: 500
- Enter a category: Food

Product added successfully