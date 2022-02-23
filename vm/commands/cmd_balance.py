import click
from vm.database.db_connection import get_connection


@click.group(help='Balance of Vending Machine')
def cli():
    pass


@cli.command(help='Put money into balance')
@click.argument('amount', type=int)
@click.pass_context
def put(ctx, amount):
    # Start transaction
    sql = get_connection()
    sql.isolation_level = None
    c = sql.cursor()
    c.execute('begin')

    try:
        ctx.obj.cus.withdraw_balance(amount=amount)
        ctx.obj.vm.add_balance(amount=amount)

        click.echo(f"Customer balance : {ctx.obj.cus.get_current_balance()}")
        click.echo(f"Vending Machine balance : {ctx.obj.vm.get_current_balance()}")

        c.execute('commit')
    except Exception as e:
        c.execute('rollback')
        click.echo(str(e))


@cli.command(help='Display balance')
@click.pass_context
def show(ctx):
    click.echo(f"Current Vending Machine balance: {ctx.obj.vm.current_vending_machine.balance}")


@cli.command(help='Withdraw all money from balance')
@click.pass_context
def withdraw(ctx):
    # Start transaction
    sql = get_connection()
    sql.isolation_level = None
    c = sql.cursor()
    c.execute('begin')
    try:
        if not ctx.obj.vm.is_balance_empty():
            current_balance = ctx.obj.vm.get_current_balance()
            ctx.obj.vm.withdraw_balance(current_balance)
            ctx.obj.cus.add_balance(current_balance)

            click.echo(f"Customer balance : {ctx.obj.cus.get_current_balance()}")
            click.echo(f"Vending Machine balance : {ctx.obj.vm.get_current_balance()}")
            c.execute('commit')
        else:
            click.echo('Balance is empty, please put money into Vending Machine first')
    except Exception:
        c.execute('rollback')
        click.echo('Error during withdraw!')
