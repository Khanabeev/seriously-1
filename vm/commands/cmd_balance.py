import click


@click.group(help='Balance of Vending Machine')
def cli():
    pass


@cli.command(help='Put money into balance')
@click.argument('amount', type=int)
@click.pass_context
def put(ctx, amount):
    click.echo(ctx.obj.vm.current_vending_machine)
    click.echo(f"You have put {amount}")


@cli.command(help='Display balance')
@click.pass_context
def show(ctx):
    click.echo(f"Current balance: {ctx.obj.vm.current_vending_machine.balance}")


@cli.command(help='Withdraw all money from balance')
@click.pass_context
def withdraw(ctx):
    try:
        if ctx.obj.vm.current_vending_machine.balance > 0:
            ctx.obj.cus.current_customer.balance += ctx.obj.vm.current_vending_machine.balance
            ctx.obj.vm.current_vending_machine.balance = 0

            ctx.obj.vm.update()
            ctx.obj.cus.update()

            click.echo(f"Customer balance : {ctx.obj.cus.current_customer.balance}")
            click.echo(f"Vending Machine balance : {ctx.obj.vm.current_vending_machine.balance}")
        else:
            click.echo('Balance is empty, please put money into VM first')
    except Exception:
        click.echo('Error during withdraw!')
