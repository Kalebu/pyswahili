
def something():
    eval(compile('b=12', '<string>', 'exec'))
    a = 23 
    c = 34
    def change():
        eval(compile('b=90', '<string>', 'exec'))

    change()
    result = eval(compile('b', '<string>', 'eval'))
    print(result)

something()