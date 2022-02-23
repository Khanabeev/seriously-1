INSERT INTO products(name, price, created_at)
VALUES ("product 1", 100, DATE()),
("product 2", 200, DATE()),
("product 3", 300, DATE());

INSERT INTO vending_machines(uid, balance, created_at)
VALUES ("vm-1", 0, DATE());

INSERT INTO product_vending_machine(vending_machine_id, product_id, created_at)
VALUES (1, 1, DATE()),
(1, 2, DATE()),
(1, 3, DATE());

INSERT INTO customers(uid, balance, created_at)
VALUES ("cus-1", 1000, DATE());