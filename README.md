# pyswahili
A programming language built over Python to easily allow swahili speakers to get started with programming without ever knowing english

[![Become a patron](pictures/become_a_patron_button.png)](https://www.patreon.com/kalebujordan)

**pyswahili** is not a completely independent language but more of a swahili version of **python language**, syntax and language grammar is 
equivalent to python one with only change of **keywords** from english to swahili. 


## pyswahili Transpiler
Transpiler(Pyswahili) is for converting the swahili version of python to english version so that it can be intepreted by the python Intepreter

## extension ?

There is no official extension for pyswahili, so for now **.py** is fine.

## Repl vs Script

Similar to Python, Pyswahili supports both modes; the Read-evaluate-print(**Repl**) loop and Script mode, 
Repl enable you to interactively execute pyswahili code line by line without requiring to write a complete program while on other side **Script mode** requires you 
to write your Pyswahili code on a file and run it as whole.

## Getting started 

To get started using Pyswahili you might need to either **clone** or **manually download** the repository 
and then use pip command to install the package just as shown below.

### Linux users 
It might require admistrator priveledge to install so use **sudo** during the installation.

```bash 
$ git clone https://github.com/Kalebu/pyswahili
$ cd pyswahili
$ sudo pip3 install -e pyswahili
```


### Window Users
If you're a Windows user, I would recommed running command prompt(cmd) with admistrator priveledge during the installation.

```powershell
$ git clone https://github.com/Kalebu/pyswahili
$ cd pyswahili
$ pip install -e pyswahili
```

## REPL MODE
Now that the pyswahili package is installed, we can start playing with it, To involve repl just run **pyswahili** without any argument 
just as shown below;

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

The Pyswahili REPL is used the same wise as the normal python repl, supporting basic statements to complex logic with block statements written in swahili, 
just as illustrated in the example below.

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
for while loop, we use the swahili keyword **wakati** instead of **while** but the syntax stays the same 
to break the loop, use keyword **vunja** 
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
In script mode, you're supposed to have write your pyswahili code in a file and then pyswahili will run it as whole, 
your code should follow pyswahili syntax (python one) for it to be evaluated.

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
[Pyswahili supported keywords](https://github.com/Kalebu/pyswahili/blob/main/pyswahili/Swahili/sw_to_en.py),
Keywords are not final, so whenever you see a need for a keyword change feel free to reach me directly.


## To Do 


- [x] Starter string based logo
- [x] Making sure only keywords are replaced
- [ ] Improving the choice of keywords 
- [ ] adding documentation + examples  
- [ ] fixing REPL bugs
- [ ] Supporting the Module structure
- [ ] Publishing Version 1.0 to the PyPI

### Ensuring Keywords are replaced

The current approach is just to replace the keywords in the whole python source code string, but the methods are error-prone 
since they also replace user defined strings, so we have to find a way whereby only keywords are being replaced. 

This can be achieved by using Python builtin **lexical scanner** tokenize for python source code, which is capable of breaking the 
python source code into pieces strings with their **type** (NAME, OP, NUMBER, NEWLINE, IDENT) and so on.

More documentation abouut tokenize can be found on its [official documentation](https://docs.python.org/3/library/tokenize.html)

Contributing
------------

Wanna contribute ? then please [contributing.md](https://github.com/Kalebu/pyswahili/blob/main/CONTRIBUTING.md) to see how


# Give it a star 

If you found this repository useful, give it a star 

You can also keep in touch with me on [Twitter](https://twitter.com/j_kalebu).


## Bug bounty?

If you encounter **issue** with the usage of the package, feel free raise an **issue** so as 
we can fix it as soon as possible(ASAP) or just reach me directly through [email](isaackeinstein@gmail.com)


*The journey has just began*
