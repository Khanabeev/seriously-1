CREATE TABLE products (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
price INTEGER NOT NULL,
created_at TEXT NOT NULL
);

CREATE TABLE customers (
id INTEGER PRIMARY KEY,
uid TEXT NOT NULL,
created_at TEXT NOT NULL
);

CREATE TABLE customer_product (
id INTEGER PRIMARY KEY,
customer_id INTEGER NOT NULL,
product_id INTEGER NOT NULL,
created_at TEXT NOT NULL,

CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE,
CONSTRAINT fk_product_id FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);