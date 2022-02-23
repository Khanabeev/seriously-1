import click


@click.command(help='Purchase a product by id')
@click.pass_context
@click.argument('product_id', type=int)
def cli(ctx, product_id):
    try:
        product_df = ctx.obj.vm.select_product(product_id)
        ctx.obj.vm.withdraw_balance(product_df["price"].values[0])
        ctx.obj.cus.add_product(product_id=product_df["id"].values[0])
        click.echo(f"You have purchased: {product_df['name'].values[0]}")
    except Exception as e:
        click.echo(str(e))
