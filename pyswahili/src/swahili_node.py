import sys
import json 

class PySwahili(object):
    def __init__(self):
        arguments = list(sys.argv)
        print(arguments)
        if len(arguments)>1:
            self.swahili_code = sys.argv[1]
        self.sw_to_en = self.load_keyword_dictionary()
        print(self.sw_to_en)


    @staticmethod
    def load_keyword_dictionary():
        try:
            with open('sw_to_english.json') as dictionary:
                print('loading dictionary')
                return json.load(dictionary)
        except FileNotFoundError:
            print('Make sure json keyword dictionary is on your current directory')
            sys.exit()
        else:
            print('Couldnt read the language dictionary')
            sys.exit()
        

    def load_python_code(self):
        try:
            with open(self.swahili_code, 'r') as pyswahili_code:
                pyswahili_string = pyswahili_code.read()
                return pyswahili_string
        except Exception as bug:
            print(bug)
            return False

    
    def convert_to_english(self, sw_python_code):
        sw_keywords = list(self.sw_to_en.keys())
        for sw_keyword in sw_keywords:
            if sw_keyword in sw_python_code:
                sw_python_code = sw_python_code.replace(sw_keyword, self.sw_to_en[sw_keyword])
        return sw_python_code


    
    def run(self):
        try:
            swahili_python_code = self.load_python_code()
            if swahili_python_code:
                english_python_code = self.convert_to_english(swahili_python_code)
                exec(english_python_code)
        except Exception as bug:
            print(bug)
