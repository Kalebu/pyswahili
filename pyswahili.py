import sys

class pyswahili(object):
    def __init__(self):
        arguments = list(sys.argv)
        if len(arguments) == 1:
            raise FileNotFoundError('No Pyswahili code specified')
        self.swahili_code = sys.argv[1]

        self.sw_to_en = {
            'ingiza': 'input',
            'kama':'if',
            'endapo': 'for',
            'imo kwenye': 'in',
            'wakati': 'while',
            'andika':'print',
            'Kweli': 'True',
            'zaidi': 'else'
        }

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



if __name__ == '__main__':
    translator_node = pyswahili()
    translator_node.run()
