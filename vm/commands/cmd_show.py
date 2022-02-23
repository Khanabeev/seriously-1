import click


@click.command(help='Display all products of Vending Machine')
@click.pass_context
def cli(ctx):
    click.echo(ctx.obj.vm.show_all_products())
