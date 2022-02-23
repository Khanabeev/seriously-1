## First assignment - Vending Machine

### Installation:

`pip install --editable .`

### How to use:

Main command `vm` opens menu with available command:

```commandline
Commands:
  balance   Balance of Vending Machine
  buy       Purchase a product by id
  customer  Show customer info
  show      Display all products of Vending Machine
```

Example of commands:

- display all product: `vm show`
- put balance to Vendor Machine: `vm balance put 100`
- withdraw balance from Vendor Machine: `vm balance withdraw`
- display balance of Vendor Machine: `vm balance show`
- show customer info: `vm customer info`
- select the product with id = 1: `vm buy 1`

### Database model:

Database: SQLite

![Image](db_image.png)