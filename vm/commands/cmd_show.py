import click

from vm.services.VendingMachine import VendingMachine


class Context:
    def __init__(self):
        self.vm = VendingMachine()


@click.command(help='Display all products of Vending Machine')
@click.pass_context
def cli(ctx):
    ctx.obj = Context()
    click.echo(ctx.obj.vm.show_all_products())
