CREATE TABLE IF NOT EXISTS products
(
  id         INTEGER PRIMARY KEY,
  name       TEXT NOT NULL,
  price      INTEGER NOT NULL,
  created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS customers
(
  id         INTEGER PRIMARY KEY,
  uid        TEXT NOT NULL,
  balance    INTEGER NOT NULL,
  created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS vending_machines
(
  id         INTEGER PRIMARY KEY,
  uid        TEXT NOT NULL,
  balance    INTEGER DEFAULT 0,
  created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS customer_product
(
  id          INTEGER PRIMARY KEY,
  customer_id INTEGER NOT NULL,
  product_id  INTEGER NOT NULL,
  created_at  TEXT NOT NULL,

CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE,
CONSTRAINT fk_product_id FOREIGN KEY(product_id) REFERENCES products(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS product_vending_machine
(
  id          INTEGER PRIMARY KEY,
  vending_machine_id INTEGER NOT NULL,
  product_id  INTEGER NOT NULL,
  created_at  TEXT NOT NULL,

CONSTRAINT fk_vending_machine_id FOREIGN KEY (vending_machine_id) REFERENCES vending_machines(id) ON DELETE CASCADE,
CONSTRAINT fk_product_id FOREIGN KEY(product_id) REFERENCES products(id) ON DELETE CASCADE
);