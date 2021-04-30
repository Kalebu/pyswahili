# pyswahili

A programming language built over Python to easily allow swahili speakers to get started with programming without ever knowing english


**pyswahili** is not a completely independent language but more of a swahili version of **python language**, syntax and language grammar is equivalent to python one with only change of **keywords** from english to swahili.


## pyswahili Transpiler

Transpiler(Pyswahili) is for converting the swahili version of python to english version so that it can be intepreted by the python Intepreter

## Extension ?

There is no official extension for pyswahili, so for now **.py** is fine.

## Repl vs Script

Similar to Python, Pyswahili supports both modes; the Read-evaluate-print(**Repl**) loop and Script mode, Repl enable you to interactively execute pyswahili code line by line without requiring to write a complete program while on other side **Script mode** requires you to write your Pyswahili code on a file and run it as whole.

## REPL MODE

Now that the pyswahili package is installed, we can start playing with it, To involve repl just run **pyswahili** without any argument just as shown below;

```bash
                 _____                         _     _ _ _ 
                |  __ \                       | |   (_) (_)
                | |__) |   _ _____      ____ _| |__  _| |_ 
                |  ___/ | | / __\ \ /\ / / _` | '_ \| | | |
                | |   | |_| \__ \\ V  V / (_| | | | | | | |
                |_|    \__, |___/ \_/\_/ \__,_|_| |_|_|_|_|
                        __/ |                              
                        |___/                               
            
author: Kalebu Jordan (github.com/kalebu)
Pyswahili 1.0 on Linux | Saturday 02, January 2021
-> 
```

### Usage

The Pyswahili REPL is used the same wise as the normal python repl, supporting basic statements to complex logic with block statements written in swahili, just as illustrated in the example below.

```python
-> a = 12
-> a
12
-> a + 89
101
-> andika('umri wako ni', a)
umri wako ni 12
-> a = a + 13
-> a
25
-> kama a%2==0:
...     andika(a, 'ni namba shufwa')
...zaidi:
...     andika(a,'ni namba witiri')
...
25 ni namba witiri
```


#### Functions in pyswahili

```python
-> njia jumla(a, b):
...     rudisha a + b 
...
-> andika(jumla(20, 21))
41
-> andika(jumla('hello ', '2021'))
hello 2021
```

## Loops Pyswahili

- while loop 
for while loop, we use the swahili keyword **wakati** instead of **while** but the syntax stays the same to break the loop, use keyword **vunja**.

```python
-> x = 3   
-> wakati x>0:
...     andika(x*10)
...     x = x - 1
...
30
20
10
```

## SCRIPT MODE

In script mode, you're supposed to have write your pyswahili code in a file and then pyswahili will run it as whole, your code should follow pyswahili syntax (python one) for it to be evaluated.

- hello.py

```python 

namba = ingiza('Namba yoyote : ')
namba = int(namba)

ikiwa no imo katiya(1, 12):
    andika(no, 'x ', namba, '=', no*namba)
```

### running script

```bash
$ pyswahili hello.py 
Namba yoyote : 8 
1 x  8 = 8
2 x  8 = 16
3 x  8 = 24
4 x  8 = 32
5 x  8 = 40
6 x  8 = 48
7 x  8 = 56
8 x  8 = 64
9 x  8 = 72
10 x  8 = 80
11 x  8 = 88
```

## SUPPORTED KEYWORDS 

If you want to see all the supported keywords in pyswahili, you can view all of them by visiting 
[Pyswahili supported keywords](https://github.com/Kalebu/pyswahili/blob/main/pyswahili/Swahili/sw_to_en.py)

Note: Keywords are not final, so whenever you see a need for a keyword change feel free to reach me directly.

## Contributing

Wanna contribute ? then please [contributing.md](https://github.com/Kalebu/pyswahili/blob/main/CONTRIBUTING.md) to see how

## Bug bounty?

If you encounter **issue** with the usage of the package, feel free raise an **issue** so as 
we can fix it as soon as possible(ASAP) or just reach me directly through isaackeinstein(at)gmail.com

## Credits

All the credits to [kalebu](https://github.com/Kalebu)