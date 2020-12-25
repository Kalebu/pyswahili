import click
from swahili_node import PySwahili
from repl import PySwahili_Repl

@click.group()
def cli():
    pass

@cli.command()
@click.argument('filename', type=str, default='')
def cli(filename):
    if filename:
        pyswahili_transpiler = PySwahili(filename=filename)
        pyswahili_transpiler.run()
    else:
        PySwahili_Repl().repl()


if __name__ == '__main__':
    cli()