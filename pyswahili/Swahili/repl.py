import json
import sys
import code
import platform
from Swahili.swahili_node import PySwahili



class PySwahili_Repl:
    def __init__(self):
        self.translator = PySwahili()
        self.block_keywords = list(self.translator.sw_to_en['block_keywords'].values())
        self.console = code.InteractiveConsole()
        self.intepreter = code.InteractiveInterpreter()
        self.newline = '\n'

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
            trimmed_line_of_code = line_of_code.replace(' ', '')
            if trimmed_line_of_code == 'else:':
                return True
            print(bug)
            return False

    def is_eval(self, line_of_code, variables):
        restricted = ['command', 'self', 'specifics']
        try:
            for var, value in variables.items():
                if all(var!=r_var for r_var in restricted):
                    assign_expression = '''{}={}'''.format(var, value)
                    eval(compile(assign_expression, '<string>', 'exec'))
            
            output = eval(compile(line_of_code, '<string>', 'eval'))
            if not line_of_code.startswith('print'):
                return output
            return True 
        except Exception as bug:
            #print(bug)
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

    @staticmethod
    def load_system_specification():
        specification = platform.uname()
        specification = 'Pyswahili 0.0.1 on {} \nBy @KalebuJordan'.format(specification.system)
        return specification

    def repl(self):
        specifics = self.load_system_specification()
        print(specifics)
        while True:
            try:
                command = self.read_user_input()
                if command:
                    if not self.newline in command:
                        evaluated = self.is_eval(command, locals())
                        if evaluated:
                            if evaluated !=True:
                                print(evaluated)
                            continue
                    eval(compile(command, '<string>', 'exec'))
                    continue
            except KeyboardInterrupt:
                sys.exit()
            
            except Exception as bug:
                print(bug)
                continue

if __name__ == '__main__':
    PySwahili_Repl().repl()
