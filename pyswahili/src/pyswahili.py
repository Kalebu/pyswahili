import json
import sys
import code 
import click
from swahili_node import PySwahili


translator = PySwahili()
console = code.InteractiveConsole()
intepreter = code.InteractiveInterpreter()


def repl():
    while True:
        try:
            swahili_command = input('>>> ')
            english_command = translator.convert_to_english(swahili_command)
            repr(console.runcode(english_command))
        except KeyboardInterrupt:
            pass
        else:
            continue

if __name__ == '__main__':
    repl()