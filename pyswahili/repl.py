import json
import sys
import ast
import code
import platform
import datetime
import traceback
from pyswahili.swahili_node import PySwahili


class PySwahili_Repl:
    def __init__(self):
        self.translator = PySwahili()
        self.block_keywords = list(
            self.translator.sw_to_en["block_keywords"].values())
        self.newline = "\n"

    @property
    def logo(self):
        return r"""       
                 _____                         _     _ _ _ 
                |  __ \                       | |   (_) (_)
                | |__) |   _ _____      ____ _| |__  _| |_ 
                |  ___/ | | / __\ \ /\ / / _` | '_ \| | | |
                | |   | |_| \__ \\ V  V / (_| | | | | | | |
                |_|    \__, |___/ \_/\_/ \__,_|_| |_|_|_|_|
                        __/ |                              
                        |___/                               
            """

    @staticmethod
    def remove_identation(line_of_code, return_number=False):
        count = 0
        while True:
            if line_of_code.startswith("\t"):
                line_of_code = line_of_code[1:]
                count += 1
                continue
            break

        if return_number:
            return count

        if not return_number:
            return line_of_code

    def is_blocky(self, line_of_code):
        return any(
            [line_of_code.startswith(keyword)
             for keyword in self.block_keywords]
        ) and line_of_code.endswith(":")

    def is_else(self, line_of_code):
        try:
            trimmed_line_of_code = line_of_code.replace(" ", "")
            if trimmed_line_of_code == "else:":
                return True
            return
        except:
            return

    def is_return(self, line_of_code):
        try:
            stripped_line_of_code = line_of_code.strip()
            if stripped_line_of_code.startswith("return "):
                return True
            return
        except:
            return

    def is_compilable(self, line_of_code):
        try:
            line_of_code = self.remove_identation(line_of_code)
            code.compile_command(line_of_code, "<string>", "exec")
            return True
        except Exception as bug:
            # print(bug)
            if self.is_else(line_of_code) or self.is_return(line_of_code):
                return True
            return False

    def is_parsable(self, line_of_code):
        try:
            line_of_code = self.remove_identation(line_of_code)
            if ast.parse(line_of_code):
                return True
        except Exception as bug:
            # print(bug)
            return False

    def is_valid(self, line_of_code):
        try:
            if self.is_compilable(line_of_code):
                # print("code is compilable")
                return True

            if self.is_parsable(line_of_code):
                # print("code is parsable")
                return True

            # print("code is not valid")
            return False
        except Exception as bug:
            traceback.print_exc()
            return False

    def is_eval(self, line_of_code, variables):
        restricted = ["command", "self", "specifics"]
        try:
            for var, value in variables.items():
                if all(var != r_var for r_var in restricted):
                    assign_expression = """{}={}""".format(var, value)
                    eval(compile(assign_expression, "<string>", "exec"))

            output = eval(compile(line_of_code, "<string>", "eval"))
            if not line_of_code.startswith("print"):
                return output
            return True
        except Exception as bug:
            # print(bug)
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
                            space_count = self.remove_identation(
                                command, return_number=True
                            )
                            english_command = self.translator.convert_to_english(
                                command
                            )
                            english_command = (
                                space_count * "\t") + english_command
                            if self.is_valid(english_command):
                                user_input = user_input + "\n" + english_command
                                continue
                        break
                return user_input
            return False

        except Exception as bug:
            print(bug)

    @property
    def load_system_specification(self):
        specification = platform.uname()
        now = datetime.datetime.now().strftime("%A %d, %B %Y")
        specification = "Pyswahili 1.0 on {} | {}".format(
            specification.system, now)
        return specification

    def repl(self):
        while True:
            try:
                command = self.read_user_input()
                if command:
                    if not self.newline in command:
                        evaluated = self.is_eval(command, locals())
                        if evaluated:
                            if evaluated != True:
                                print(evaluated)
                            continue
                    # print(command)
                    exec(command, globals())
                    continue
            except KeyboardInterrupt:
                sys.exit()

            except Exception as bug:
                print(bug)
                continue


if __name__ == "__main__":
    PySwahili_Repl().repl()
