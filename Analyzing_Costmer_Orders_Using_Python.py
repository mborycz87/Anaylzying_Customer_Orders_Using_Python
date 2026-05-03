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

# Task 3: Calculate spending and classify customers

# Use a loop to calculate the total amount each customer spends
customer_spending = {}
for name, product, price, category in orders:
    customer_spending[name] = customer_spending.get(name, 0) + price
    
for key, value in customer_spending.items():
    print(f" {key} spent ${value:,.2f}")

"""
• If the total purchase value is above $100, classify the customer as a high-value buyer 
• If it is between $50 and $100, classify the customer as a moderate buyer 
• If it is below $50, classify them as a low-value buyer 
"""
for name, spent in customer_spending.items():
    if spent > 100:
        customer_value = "high-value buyer"
    elif 5 <= spent <= 100:
        customer_value = "moderate buyer"
    else:
        customer_value = "low-value buyer"
    print(f"The customer {name} spent ${spent:,.2f}. Making them a {customer_value} customer.")

# Calculate the total revenue per product category and store it in a dictionary
print("Calculate the total revenue per product category and store it in a dictionary.\n")
revenue_per_category ={}
for name, product, price, category in orders:
    revenue_per_category[category] = revenue_per_category.get(category, 0) + price

for categorys, cost in revenue_per_category.items():
    print(f"The {categorys} category made a total of ${cost:,.2f} in revenue.") 

# Extract unique products from all orders using a set
print("\nExtract unique products from all orders using a set.\n")
unique_products = set()
for name, product, price, category in orders:
    unique_products.add(product)
for products in unique_products:
    print(f"One unique product is: {products}")
    
# Use a list comprehension to find all customers who purchased electronics
print("\nUse a list comprehension to find all customers who purchased electronics\n")
electronics_buyers = []
for name, product, price, category in orders:
    if category == "Electronics":
        electronics_buyers.append(name)
for buyer in electronics_buyers:
    print(f"{buyer} bought electronics.")

# Identify the top three highest-spending customers using sorting
print("\nIdentify the top three highest-spending customers using sorting\n")
top_three_buyers = sorted(customer_spending.items(), key=lambda x: x[1], reverse = True)
counter = 1
for buyers in top_three_buyers:
    if counter <= 3:
        print(f"{buyers[0]} is the number {counter} customer.")
        counter += 1