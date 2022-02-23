import click


@click.command(help='Select product id')
@click.pass_context
@click.argument('product_id', type=int)
def cli(ctx, product_id):
    pass
