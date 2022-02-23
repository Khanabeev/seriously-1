import click

from vm.services.VendingMachine import VendingMachine


class Context:
    def __init__(self, product: int):
        self.product = product
        self.vm = VendingMachine()


@click.group(help='Select product')
@click.option('-p', '--product', type=int, help='Product number')
@click.pass_context
def cli(ctx, product):
    """Select product"""
    ctx.obj = Context(product)


@cli.command()
@click.pass_context
def current(ctx):
    result = ctx.obj.vm.add_product(product=ctx.obj.product)

