import os
import click
from Swahili.swahili_node import PySwahili
from Swahili.repl import PySwahili_Repl

@click.command()
@click.argument('filename', type=str, default='')
def cli(filename):
    if filename:
        pyswahili_transpiler = PySwahili(filename=filename)
        pyswahili_transpiler.run()
    else:
        PySwahili_Repl().repl()


if __name__ == '__main__':
    cli()