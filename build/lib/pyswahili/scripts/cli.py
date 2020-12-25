import os
print(os.listdir())
import click
from pyswahili.swahili_node import PySwahili
from pyswahili.repl import PySwahili_Repl
print('damn')

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