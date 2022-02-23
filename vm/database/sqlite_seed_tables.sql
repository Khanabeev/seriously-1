INSERT INTO products(name, price, created_at)
VALUES ("product 1", 100, DATE()),
("product 2", 200, DATE()),
("product 3", 300, DATE());

INSERT INTO vending_machines(uid, balance, created_at)
VALUES ("vm-1", 0, DATE());

INSERT INTO customers(uid, balance, created_at)
VALUES ("cus-1", 1000, DATE());