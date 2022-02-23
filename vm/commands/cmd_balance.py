import click


@click.group(help='Balance of Vending Machine')
def cli():
    pass


@cli.command(help='Put money into balance')
@click.argument('amount', type=int)
@click.pass_context
def put(ctx, amount):
    click.echo(ctx.obj.vm)
    click.echo(f"You have put {amount}")


@cli.command(help='Display balance')
@click.pass_context
def show(ctx):
    click.echo(f"Current balance: {ctx.obj.vm.current_vending_machine.balance}")


@cli.command(help='Withdraw all money from balance')
@click.pass_context
def withdraw(ctx):
    try:
        if not ctx.obj.vm.is_balance_empty():
            ctx.obj.cus.add_money(ctx.obj.vm.withdraw_money())

            click.echo(f"Customer balance : {ctx.obj.cus.get_current_balance()}")
            click.echo(f"Vending Machine balance : {ctx.obj.vm.get_current_balance()}")
        else:
            click.echo('Balance is empty, please put money into Vending Machine first')
    except Exception:
        click.echo('Error during withdraw!')
