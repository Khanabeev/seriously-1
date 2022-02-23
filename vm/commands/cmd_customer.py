import click

from vm.services.VendingMachineService import VendingMachineService


@click.group(help='Show customer info')
@click.pass_context
def cli(ctx):
    pass


@cli.command()
@click.pass_context
def info(ctx):
    click.echo(ctx.obj.cus.show_info())
