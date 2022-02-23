import click


@click.command(help='Select product by id')
@click.pass_context
@click.argument('product_id', type=int)
def cli(ctx, product_id):
    try:
        product_df = ctx.obj.vm.select_product(product_id)
        ctx.obj.vm.withdraw_balance(product_df["price"].values[0])
    except Exception as e:
        click.echo(getattr(e, 'message', str(e)))
