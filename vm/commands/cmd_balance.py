import click

from vm.services.VendingMachine import VendingMachine


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
def show():
    click.echo(f"This is a balance of VM")


@cli.command(help='Withdraw all money from balance')
def withdraw():
    click.echo(f"This is a balance of VM")
