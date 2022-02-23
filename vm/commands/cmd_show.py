import click

from vm.services.VendingMachine import VendingMachine


@click.command(help='Display all products of Vending Machine')
@click.pass_context
def cli(ctx):
    click.echo(ctx.obj.vm.show_all_products())
