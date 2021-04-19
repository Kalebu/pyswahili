import io
import os
import sys
import json
import tokenize
from pyswahili.sw_to_en import dictionary


class PySwahili(object):
    def __init__(self, filename=""):
        if filename:
            self.swahili_code = filename
        self.sw_to_en = dictionary

    def load_python_code(self) -> str:
        try:
            if os.path.isfile(self.swahili_code):
                with open(self.swahili_code, "r") as pyswahili_code:
                    return pyswahili_code.read()
            raise FileNotFoundError(
                "Can't find a path to {}".format(self.swahili_code))
        except Exception as bug:
            print(bug)
            return ""

    def create_english_tokens(self, sw_python_code):

        sw_to_en = self.sw_to_en["keywords"]
        sw_keywords = list(sw_to_en.keys())
        tokens = tokenize.generate_tokens(sw_python_code)

        for token in tokens:
            token_string = token.string
            if token.type == 1 and token_string in sw_keywords:
                token_string = sw_to_en.get(token_string, token_string)
            yield token.type, token_string

    def convert_to_english(self, sw_python_code):
        try:
            sw_python_code = io.StringIO(sw_python_code).readline
            all_tokens = self.create_english_tokens(sw_python_code)
            return tokenize.untokenize(all_tokens)
        except Exception as bug:
            print(bug)
            return

    def run(self):
        try:
            swahili_python_code = self.load_python_code()
            if swahili_python_code:
                english_python_code = self.convert_to_english(
                    swahili_python_code)
                exec(english_python_code)
        except Exception as bug:
            print(bug)
