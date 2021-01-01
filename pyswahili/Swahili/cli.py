import os
import click
from Swahili.swahili_node import PySwahili
from Swahili.repl import PySwahili_Repl


@click.command()
@click.argument("filename", type=str, default="")
def cli(filename):
    if filename:
        pyswahili_transpiler = PySwahili(filename=filename)
        pyswahili_transpiler.run()
    else:
        repl = PySwahili_Repl()
        click.secho(repl.logo, fg="green")
        click.secho("author: Kalebu Jordan (github.com/kalebu)", fg="green")
        click.secho(repl.load_system_specification, fg="magenta")
        repl.repl()


if __name__ == "__main__":
    cli()