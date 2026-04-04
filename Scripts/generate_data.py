import pandas as pd
import random
from datetime import datetime, timedelta

# Load products
products = pd.read_csv("../data/processed/products_clean.csv")

# ------------------ CUSTOMERS ------------------ #

num_customers = 200

customers = pd.DataFrame({
    "customer_id": range(1, num_customers + 1),
    "customer_name": [f"Customer_{i}" for i in range(1, num_customers + 1)],
    "city": [random.choice(["Delhi", "Mumbai", "Kolkata", "Bangalore"]) for _ in range(num_customers)],
    "signup_date": [datetime.today() - timedelta(days=random.randint(30, 365)) for _ in range(num_customers)]
})

# ------------------ ORDERS ------------------ #

num_orders = 1000

orders = []

for i in range(1, num_orders + 1):
    customer_id = random.randint(1, num_customers)
    order_date = datetime.today() - timedelta(days=random.randint(1, 90))

    orders.append([i, customer_id, order_date])

orders = pd.DataFrame(orders, columns=["order_id", "customer_id", "order_date"])

# ------------------ ORDER ITEMS ------------------ #

order_items = []

for order_id in orders['order_id']:
    num_items = random.randint(1, 3)

    for _ in range(num_items):
        product = products.sample(1).iloc[0]

        quantity = random.randint(1, 5)

        order_items.append([
            order_id,
            product['product_id'],
            quantity,
            product['price']
        ])

order_items = pd.DataFrame(order_items, columns=[
    "order_id", "product_id", "quantity", "price"
])

# ------------------ SAVE FILES ------------------ #

customers.to_csv("../data/processed/customers.csv", index=False)
orders.to_csv("../data/processed/orders.csv", index=False)
order_items.to_csv("../data/processed/order_items.csv", index=False)

print("✅ Customers, Orders, and Order Items generated!")