## First assignment - Vending Machine

### Installation:

- install dependencies `pip install --editable .`
- initialize database `python vm/database/init_db.py `

### How to use:

`vm` opens menu with the available command:

```commandline
Commands:
  balance   Balance of Vending Machine
  buy       Purchase a product by id
  customer  Show customer info
  show      Display all products of Vending Machine
```

Example:

- display all products: `vm show`
- put balance to a Vendor Machine: `vm balance put 100`
- withdraw a balance from Vending Machine: `vm balance withdraw`
- display a balance of Vendor Machine: `vm balance show`
- show customer info: `vm customer info`
- buy a product with id = 1: `vm buy 1`

### Database model:

Database: SQLite

![Image](db_image.png)

### Scalability

If an application gets bigger there are a few solutions that can help to scale it:

- Database, `vending_machine_service.py` and `customer_service.py` are ready for multiple customers and vending machines
  entries. If it's necessary we can add a command like `vm set vending_machine <uid>` or `vm set customer <uid>` in
  order to change customer or vending machine;
- Due to `vending_machine_repository.py`,`customer_repository.py`, and `product_repository.py` we can implement
  different databases, for instance, we can replace SQLite with PostgreSQL;
- Inside `db_connection.py` we can change the connection to another database. Due to the fact that we have used only SQL
  queries in repositories, change connection might be easy. Besides, we can replace `sqlite3` package with a more
  sophisticated `sqlalchemy`;
- New commands are automatically parsed in `vm/commands` directory;
- If someday we want to change the seed script for the database, we will need to upload it to `vm/database` directory
  and indicate a filename in config (if we rename it of course);
- We should set environment variables (like `export NEW_VAR=new_variable`) in order to configure our app from outside
  and don't touch the code. 
