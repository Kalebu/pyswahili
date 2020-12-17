# pyswahili
A programming language to built on top of Python to easily allow swahili speakers to get started with programming without ever knowing english


## Compiled or interpreted ?
The choice whether the pyswahili language to be either compiled language or interpreted still in analysis so keep an eye to this repo.

## To DO

This will involve designing a **pyswahili Intepreter** on top of Python to parse and interpret pyswahili statement 
, condition, loops , and much more.

The Goal now is to support the following features for the language

- [ ] Designing a language syntax 
- [ ] Simple Arithmetic Operation
- [ ] conditionals  
- [ ] loops
- [ ] Functions 
- [ ] Object Oriented 


## Building a language bridge 

Jus gota an idea from a well experienced Pythonista that I do not have to re-implement the whole language instead I could write some kinda
of a node to acts as bridge between all the english keywords and swahili keywords,

implemented a small piece of code for the initial node(waiting heavily modification).

How to run a pyswahili code 

```Python
umri = ingiza('Umri wako: ')
umri = int(umri)

kama umri < 18:
  andika('bado kijana mdogo')
zaidi:
  andika('sasa waweza date')
```
You can save your **pyswahili** code with just **.py** extension.

To run your code is just straight forward as following

```bash
kalebu@kalebu-PC pyswahili -> python3 pyswahili.py hello.py 
bado kijana mdogo
```


*The journey has just began*