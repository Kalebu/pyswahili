import json
import sys
import code 
import click
from swahili_node import PySwahili


translator = PySwahili()
block_keywords = list(translator.sw_to_en['block_keywords'].values())
console = code.InteractiveConsole()
intepreter = code.InteractiveInterpreter()

def remove_identation(line_of_code):
    while True:
        if line_of_code.startswith('\t'):
            line_of_code = line_of_code[1:]
            continue
        break
    return line_of_code


def is_blocky(line_of_code):
    return any([line_of_code.startswith(keyword) for keyword in block_keywords]) and line_of_code.endswith(':')

def is_valid(line_of_code):
    try:
        line_of_code = remove_identation(line_of_code)
        code.compile_command(line_of_code)
        return True 
    except Exception as bug:
        print(bug)
        return False

def read():
    try:
        user_input = ""
        command = input(">>> ")
        english_command = translator.convert_to_english(command)
        if is_valid(english_command):
            user_input = english_command
            if is_blocky(english_command):
                while True:
                    command = input("...")
                    if command:
                        english_command = translator.convert_to_english(command)
                        if is_valid(english_command):        
                            user_input = user_input + "\n" + english_command
                            continue
                    break
            return user_input
        return False

    except Exception as bug:
        print(bug)


def repl():
    while True:
        try:
            command = read()
            if command:
                repr(console.runcode(command))
                continue
            print('umeokosea sarufi')
        except KeyboardInterrupt:
            pass
        else:
            continue

if __name__ == '__main__':
    repl()
