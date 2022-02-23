## First assignment - Vending Machine

### Installation:
- install dependencies `pip install --editable .`
- initiate database `python vm/database/init_db.py `


### How to use:

`vm` opens menu with available command:

```commandline
Commands:
  balance   Balance of Vending Machine
  buy       Purchase a product by id
  customer  Show customer info
  show      Display all products of Vending Machine
```

Example:

- display all product: `vm show`
- put balance to a Vendor Machine: `vm balance put 100`
- withdraw a balance from Vending Machine: `vm balance withdraw`
- display a balance of Vendor Machine: `vm balance show`
- show customer info: `vm customer info`
- buy a product with id = 1: `vm buy 1`

### Database model:

Database: SQLite

![Image](db_image.png)