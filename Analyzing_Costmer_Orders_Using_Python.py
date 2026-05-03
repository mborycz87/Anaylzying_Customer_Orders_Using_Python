"""
1. Store customer orders 
• Create a list of customer names 
• Store each customer's order details (customer name, product, price, category) as 
tuples inside a list 
• Use a dictionary where keys are customer names and values are lists of ordered 
products 
"""

# Task 1: Store customer names and order details as tuples in a list
orders = [
    ("Alice", "Laptop", 1200, "Electronics"),
    ("Bob", "Shirt", 25, "Clothing"),
    ("Charlie", "Toaster", 45, "Home Essentials"),
    ("Alice", "Mouse", 25, "Electronics"),
    ("Bob", "Jeans", 50, "Clothing"),
    ("David", "Smartwatch", 150, "Electronics")
]

# Make a dictionary mapping names to lists of products
customer_orders = {}
for name, product, price, category in orders:
    if name not in customer_orders:
        customer_orders[name] = []
    customer_orders[name].append(product)
    
for key, value in customer_orders.items():
    print(f"This customer's name is: {key} they ordered {value}")

# Task 2: Map products to categories and find unique categories

# Use a dictionary to map each product to its respective category
categorized_products = {}
for name, product, price, category in orders:
    if product not in categorize_products:
        categorized_products[product] = []
    categorized_products[product].append(category)
    
for key, value in categorized_products.items():
    print(f" This is the item: {key} and this is it's catagory: {value}")

# Create a set of unique product categories
unique_categories = set()
for name, product, price, category in orders:
    if category not in unique_categories:
        unique_categories.add(category)

print(f"\nAll availabel product categories are: {unique_categories}")