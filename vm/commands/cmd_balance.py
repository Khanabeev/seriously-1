import click

from vm.services.VendingMachine import VendingMachine


class Context:
    def __init__(self):
        self.vm = VendingMachine()


@click.group(help='Balance of Vending Machine')
@click.pass_context
def cli(ctx):
    ctx.obj = Context()


@cli.command(help='Put money into balance')
@click.argument('amount', type=int)
def put(amount):
    click.echo(f"You have put {amount}")


@cli.command(help='Display balance')
def show():
    click.echo(f"This is a balance of VM")


@cli.command(help='Withdraw all money from balance')
def withdraw():
    click.echo(f"This is a balance of VM")
