import json
import sys
import code 
import click
from swahili_node import PySwahili



class PySwahili_Repl:
    def __init__(self):
        self.translator = PySwahili()
        self.block_keywords = list(self.translator.sw_to_en['block_keywords'].values())
        self.console = code.InteractiveConsole()
        self.intepreter = code.InteractiveInterpreter()

    @staticmethod
    def remove_identation(line_of_code):
        while True:
            if line_of_code.startswith('\t'):
                line_of_code = line_of_code[1:]
                continue
            break
        return line_of_code

    def is_blocky(self, line_of_code):
        return any([line_of_code.startswith(keyword) for keyword in self.block_keywords]) and line_of_code.endswith(':')

    def is_valid(self, line_of_code):
        try:
            line_of_code = self.remove_identation(line_of_code)
            code.compile_command(line_of_code)
            return True 
        except Exception as bug:
            print(bug)
            return False

    def read_user_input(self):
        try:
            user_input = ""
            command = input(">>> ")
            english_command = self.translator.convert_to_english(command)
            if self.is_valid(english_command):
                user_input = english_command
                if self.is_blocky(english_command):
                    while True:
                        command = input("...")
                        if command:
                            english_command = self.translator.convert_to_english(command)
                            if self.is_valid(english_command):        
                                user_input = user_input + "\n" + english_command
                                continue
                        break
                return user_input
            return False

        except Exception as bug:
            print(bug)


    def repl(self):
        print('Pyswahili 0.0.1 by @kalebujordan')
        while True:
            try:
                command = self.read_user_input()
                if command:
                    repr(self.console.runcode(command))
                    continue
            except KeyboardInterrupt:
                sys.exit()
            else:
                continue

if __name__ == '__main__':
    PySwahili_Repl().repl()
