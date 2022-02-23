import click


@click.group(help='Balance of Vending Machine')
def cli():
    pass


@cli.command(help='Put money into balance')
@click.argument('amount', type=int)
@click.pass_context
def put(ctx, amount):
    click.echo(ctx.obj.vm.current_vending_machine_id)
    click.echo(f"You have put {amount}")


@cli.command(help='Display balance')
@click.pass_context
def show(ctx):
    click.echo(f"Current balance: {ctx.obj.vm.current_vending_machine.balance}")


@cli.command(help='Withdraw all money from balance')
@click.pass_context
def withdraw(ctx):
    if ctx.obj.vm.current_vending_machine.balance > 0:
        click.echo('Add to customer balance')
    else:
        click.echo('Balance is empty, please put money into VM first')
