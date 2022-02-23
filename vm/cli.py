import os

import click

from vm.services.CustomerService import CustomerService
from vm.services.VendingMachineService import VendingMachineService


class Context:
    def __init__(self):
        self.vm = VendingMachineService()
        self.cus = CustomerService()


class ComplexCLI(click.MultiCommand):
    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(os.path.join(os.path.dirname(__file__), "commands")):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            mod = __import__(f"vm.commands.cmd_{name}", None, None, ["cli"])
        except ImportError:
            return
        return mod.cli


@click.command(cls=ComplexCLI)
@click.pass_context
def cli(ctx):
    """ === Welcome to Vending Machine ==="""
    ctx.obj = Context()
