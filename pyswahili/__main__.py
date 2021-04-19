import os
import sys
import argparse
from pyswahili.repl import PySwahili_Repl
from pyswahili.swahili_node import PySwahili


class App():
    def __init__(self):
        self.pyswahili_parser = argparse.ArgumentParser(
            description="Pyswahili Repl application")
        self.pyswahili_parser.add_argument('python_script', default="launch", type=str,
                                           help="Specify the script you would like pyswahili to run", nargs='?')

    def run(self):
        args = self.pyswahili_parser.parse_args()
        script_filename = args.python_script
        if script_filename == 'launch':
            self.launch_repl()
            return
        self.run_script(script_filename)

    def run_script(self, filename: str):

        if not os.path.isfile(filename):
            print(f'{filename} Does not exist or is not a file')

        active_repl = PySwahili(filename)
        active_repl.run()

    @staticmethod
    def launch_repl():
        repl = PySwahili_Repl()
        print(repl.logo)
        print(repl.load_system_specification)
        repl.repl()


def main(args=None):
    """The main routine."""
    App().run()


if __name__ == "__main__":
    sys.exit(main())
