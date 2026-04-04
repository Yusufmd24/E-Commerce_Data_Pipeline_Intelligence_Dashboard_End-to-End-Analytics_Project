CREATE DATABASE ecommerce_db;
Go

USE ecommerce_db;

-- Customers
ALTER TABLE customers
ADD CONSTRAINT pk_customers PRIMARY KEY (customer_id);

-- Products
ALTER TABLE products_clean
ADD CONSTRAINT pk_products PRIMARY KEY (product_id);

-- Orders
ALTER TABLE orders
ADD CONSTRAINT pk_orders PRIMARY KEY (order_id);

-- Orders → Customers
ALTER TABLE orders
ADD CONSTRAINT fk_customer
FOREIGN KEY (customer_id) REFERENCES customers(customer_id);

-- Order Items → Orders
ALTER TABLE order_items
ADD CONSTRAINT fk_order
FOREIGN KEY (order_id) REFERENCES orders(order_id);

-- Order Items → Products
ALTER TABLE order_items
ADD CONSTRAINT fk_product
FOREIGN KEY (product_id) REFERENCES products_clean(product_id);

--- Business Queries ---

--Total Revenue
SELECT 
    SUM(quantity * price) AS total_revenue
FROM order_items;

-- Top Products
SELECT TOP 5
    p.product_name,
    SUM(oi.quantity * oi.price) AS revenue
FROM order_items oi
JOIN products_clean p 
    ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC;

-- Top Customers
SELECT TOP 5
    c.customer_name,
    SUM(oi.quantity * oi.price) AS total_spent
FROM customers c
JOIN orders o 
    ON c.customer_id = o.customer_id
JOIN order_items oi 
    ON o.order_id = oi.order_id
GROUP BY c.customer_name
ORDER BY total_spent DESC;

-- Category Revenue
SELECT 
    p.category,
    SUM(oi.quantity * oi.price) AS revenue
FROM order_items oi
JOIN products_clean p 
    ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;