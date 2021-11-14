from platform import python_version
from itertools import zip_longest
import itertools
import math
from typing import final
print('Hello World!')

num = int(input())
a, b = 1, 2 # a = 1, b = 2

def numbers():
  return 1, 2, 3, 4, 5

a, b, c, d, e = numbers()

print(3 + 2) # 5    +=
print(3 - 2) # 1    -=
print(3 * 2) # 6    *=
print(3 / 2) # 1.5  /=
print(2 / 2) # 1.0
print(2**3)  # 8   **=
print(7 // 2)# 3   //=
print(7 % 2) # 1    %=

print('uma')
print("duas")
print('''uma
duas
tres linhas''')
print(f'interpolado {num}')
"""
  docstring
"""

print('spam' + 'eggs') # spameggs
print('2' + '3') # 23
# print('2' + 2) # error
print('2' * 4) # 2222

print(1 == 1) # True
print(1 != 1) # False
print(2 >= 1) # True
print(2 <= 1) # False
print(2 > 1)  # True
print(2 < 1)  # False

print(1 > 0 and 2 < 1) # False
print(1 > 0 or 2 < 1)  # True
print(not (1 > 0 and 2 < 1)) # True
print(not None) # true # implicit values
print(not []) # true # but [] != None

str = []
# print(len(str) == 0) # not python way
print(not str) # empty, None or zero
# also as
print(str is None) # anything but None
print(str is not None) # only None

if num > 10:
  print(f'{num} é maior que 10')
elif num == 10:
  print(f'{num} é igual a 10')
else:
  print(f'{num} é menor que 10')

while num > 0:
  print(num)
  num -= 1;

words = ['hello', 'world', '!']
str = 'Hello World!'
m = [
  [1, 2, 3],
  [4, 5, 6]
]
print(words[2]) # !
print(str[6]) # W
print(words + [1, 2, 3]) # ['hello', 'world', '!', 1, 2, 3]
print([1, 2, 3] + [4, 5, 6]) # [1, 2, 3, 4, 5, 6]
print([1, 2, 3].extend([4, 5, 6]))

ord('a') # unicode value

print('hello' in words) # True
print(4 not in [1, 2, 3]) # True

for w in words:
  print(f'{w}!')

print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(3, 8))) # [3, 4, 5, 6, 7]
print(list(range(2, 10, 3))) # [2, 5, 8]

words = [1, 'a', 2, 'a', 3, 'a', 4, 'a', 5, 'a']
for i in range(words.count('a')):
  words.remove('a')
  print(words)

words = [1, 'a', 2, 'a', 3, 'a', 4, 'a', 5, 'a']
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6]) # [4, 9, 16, 25]
print(squares[3:8]) # [9, 16, 25, 36, 49]
print(squares[0:1]) # [0]
print(squares[:7])  # [0, 1, 4, 9, 16, 25, 36]
print(squares[7:])  # [49, 64, 81]
print(squares[::2]) # [0, 4, 16, 36, 64]
print(squares[2:8:3])#[4, 25]
print(squares[1:-1])# [1, 4, 9, 16, 25, 36, 49, 64]
print(squares[-1])  # 81
print(squares[::-1])# [81, 64, 49, 36, 25, 16, 9, 4, 1, 0]
# same as list.reverse()
# same as reversed(list)

len(squares) # 10
squares.append(100) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
squares.insert(0,'fon') # ['fon', 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
squares.index(9) # 4
[3, 1, 2].sort() # [1, 2, 3]

max([1, 2, 3, 4, 5]) # 5
min([1, 2, 3, 4, 5]) # 1
words.count('a') # 5
squares.remove('fon') # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[1, 2, 3].reverse() # [3, 2, 1]

nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg) # Numbers: 4 5 6
a = "{x}, {y}".format(x=5, y=12)
print(a) # 5, 12

print(", ".join(["spam", "eggs", "ham"])) # prints "spam, eggs, ham"
print("Hello ME".replace("ME", "world")) # prints "Hello world"
print("This is a sentence.".startswith("This")) # prints "True"
print("This is a sentence.".endswith("sentence.")) # prints "True"
print("This is a sentence.".upper()) # prints "THIS IS A SENTENCE."
print("AN ALL CAPS SENTENCE".lower()) # prints "an all caps sentence"
print("spam, eggs, ham".split(", ")) # prints "['spam', 'eggs', 'ham']"

def main(n):
  return n + 1
print(main(num))

# file != script
def main():
  print('Hello World!')
  print('im not a file, im a script!')
if __name__ == '__main__':
  main() # prevents from runing scripts when importing
  _ = 'dont use me!'

import time
import traceback

# while True:
#   try:
#     print('Vrummmmmmm')
#     time.sleep(0.1)
#     raise Exception('que')
#   except Exception: # != 'exception', excludes keyboardinterrupt (^C)
#     print('unheeeee')

try:
  raise Exception('unheeee')
except Exception as e:
  print(e)
  traceback.print_exc() # keeps track of the trouble
  print(traceback.format_exc)

print('ALWAYS MAKE LISTS AS SETs OR HASH TABLES')

def fun(str, arr=None): # prevents reassigning the arr im memory
  if isinstance(arr, type(None)):
    arr = []
  for s in str:
    arr.append(s)
  return arr
# better way to assign arrays

# python -i file.py

# import pdb
# pdb.set_trace()
# debug code

# $ pip install virtual env
# $ virtualenv venv
# $ source venv/bin/activate
# # also as
# $ python -m venv my_venv
# $ python file.py // python -m file

fruits = [
  {'name': 'apple', 'price': 20},
  {'name': 'avocado', 'price': 10},
  {'name': 'orange', 'price': 5}
] # Dictionary

print(
  # list comprehension
  [fruit['name'] for fruit in fruits if fruit['name'][0] == 'a']
) # ['apple', 'avocado']

print(
  {fruit['name']: fruit['price'] for fruit in fruits}
) # {'apple': 20, 'avocado': 10, 'orange': 5}

add: lambda x,y: x + y # lambda anonymous function

# more_than_one_nums = filter(lambda x: x > 1, [1, 2, 3]) # inline functions
# print(more_than_one_nums)

condition = True
x = 1 if condition else 0
# ternary

num1 = 10_000_000_000
num2 = 100_000_000 # grouping numbers w/o messing code
total = num1 + num2
print(f'{total:,}') # 10,100,000,000

# context manager
# with open('file', 'r') as f:
#   content = f.raed()
# print(len(content.split(' ')))
# better way to manage resources

names = ['Otávio', 'Pedro', 'Marina', 'Alex']
apelidos = ['Ota', 'Pepe', 'Nina', 'Alek']

for index, name in enumerate(names, start=1):
  print(index, name)
# enumarete function, same as JavaScript forEach

for name, apelido in zip(names, apelidos):
  print(f'O apelido do {name} é {apelido}')

# packinhg and unpacking

# normal
items = (1, 2)
print(items) # (1, 2)

# umpacking

# a, b = (1, 2)
a, _ = (1, 2) # _ as variable is ignored by the code
print(a) # 1
# print(b) # 2

# a, b, c = (1, 2) # error, not enough values to unpack
# a, b = (1, 2, 3) # error, not enough variables to assign

a, b, *c, d = (1, 2, 3, 4, 5, 6, 7)
print(a) # 1
print(b) # 2
print(c) # [3, 4, 5, 6] # all unassigned values # can be set as _ too
print(d) # 7 # last value

class Person(): # Object
  pass

person = Person()

# person.first = 'Otávio'
# person.last = 'Pedro'

# first_key = 'first'
# first_val = 'Pedro'

# setattr(person, first_key, first_val)
# first = getattr(person, first_key)
# uses functions to set/get keys and values from a object

for fruit in fruits:
  for key, value in fruit.items():
    setattr(person, key, value)
  print(person.name, person.price)

# for key in person.keys():
#   print(getattr(person, key))

from getpass import getpass
username = input('Username: ')
password = getpass('Password: ')
print('Logging In...')
#set a get password function, hiding the input

# help(module_name)

from datetime import datetime
dir(datetime)
datetime.today
datetime.today()
now = datetime.now()
print(now.day, now.month, now.year, now.hour, now.minute, now.second)

# contdown
now = datetime.now()
end = datetime(2020, 12, 1)
print((end-now).microseconds) # aaa

# elapsed time
start = datetime.now()

for i in range(100_000_000):  # to pass time
  pass

end = datetime.now()

print(type(end-start)) # <class 'datetime.timedelta'>
elapsed = end-start
print(elapsed)
print(elapsed.seconds, elapsed.microseconds)

print(f"\033[91mError: This is \033[96mcyan. \033[92mContinue?")
# Colored Text

print(round(8.5)) #down to 8
print(round(9.5)) #up to 10

# import webbrowser
# webbrowser.open('github.com/pedromchd')

msg = 'message ' 'other message'
print(msg) # message other message
print('message '
      'other message')
# message other message
print('''message \
      other message
      another message''')
# message other message
# another message

if 'Git' in 'GitHub': print('GitHub'.index('Git')) # may cause errors

'GitHub'.find('Git') # sames as .index()

fruit = {'Orange': 15}
print(id(fruit)) # gets unique id from objetct

# use as an alias
dict1 = {'a': 1, 'b': 2}
dict2 = dict1
dict2['c'] = 3
print(id(dict1) == id(dict2)) # true
print(dict1) # {'a': 1, 'b': 2, 'c': 3}
print(dict2) # {'a': 1, 'b': 2, 'c': 3}
# doesnt work in primary values

# actually copy
dict1 = {'a': 1, 'b': 2}
dict2 = dict1[:]
# same as dict1.copy()
dict2['c'] = 3
print(id(dict1) == id(dict2)) # false
print(dict1) # {'a': 1, 'b': 2}
print(dict2) # {'a': 1, 'b': 2, 'c': 3}

# actually replaces content
dict1[:] = dict2
print(dict1) # {'a': 1, 'b': 2, 'c': 3}
print(dict2) # {'a': 1, 'b': 2, 'c': 3}

from copy import deepcopy

tech = ['C++', 'Go', 'Python', ['html', 'css', 'pics']]
learning = tech.copy()
print(id(tech) == id(learning)) # false
print(id(tech[-1]) == id(learning[-1])) #true with shallow copy

learning = deepcopy(tech)
print(id(tech) == id(learning)) # false
print(id(tech[-1]) == id(learning[-1])) # false

age = 16
print('age' in locals(), 'age' in globals())
del age
print('age' in locals(), 'age' in globals())
age = None
print('age' in locals(), 'age' in globals())

for language in ['C', 'C++', 'Java', 'C#', 'Python', 'Go', 'Rust']:
    print(language, end=" ") # end=' ' changes ending of line output
print("") #to go to next line for the next output

print(fruits, names, tech)

# use else in loops
for name in names:
  if name == 'Rafaela': apelidos.append('Rafa')
  break
else:
  print('Cade a Rafa???')

print(list(range(0, 100, 3)))

def letters(x, y, z):
  print(f'the letters are {x}, {y} and {z}')

lett = ['a', 'b', 'c']
letters(*lett) # * gets all unassigned elements

def nothing():
  pass # does nothing

words = list(set(words)) # remove duplicates
words = [1, 2, 3, 4, 5, 'a']

day = 'Sunday'
if day in ['Saturday', 'Sunday']: print('its weekend')

conditions = [True, False]
if any(conditions): print('same as "or"')
if all(conditions): pass
else: print('same as "and"')

full_name = "Caleb Curry"
# returns list but can assign to individual variables
first, last = full_name.split()
print(first, last)

data = "1 2 3"
data = [int(d) for d in data.split()]
print(data)

#This is most useful to get multiple inputs separated by spaces:
#first, last = input().split()

pets = ['dog', 'dog', 'cat', 'bird', 'cat', 'chicken', 'cat', 'dog']

clean_pets = [pet for pet in pets if pet not in ['cat', 'chicken']]
print(clean_pets)
# ['dog', 'dog', 'bird', 'dog']

# no do-while in python

# assign a functin to a variable
var_main = main # dont use ()

# time.sleep(1) # wait whit import time // time.sleep

pairs = [[5, 10],[15, 20],[25, 30, 35, 40]]
flat_list = [item for pair in pairs for item in pair]
# [5, 10, 15, 20, 25, 30, 35, 40]

# Wrapping a Primitive to change within function
# Class parenthesis optional but not function parenthesis
# The() are optional for classes. Only needed if you're inheriting. However, function() are always required when defining.
class Container:
  def __init__(self, data):
    self.data = data

def calculate(input):
  input.data **= 5

container = Container(5)
calculate(container)
print(container.data) # 3125

c1 = Container(5)
c2 = Container(5)
print(c1 is c2) #better code # false
print(c1 == c2) # same values
print(c1 is c2) # different objects

# Add a method dynamically
def __eq__(self, other):
  return self.data == other.data
Container.__eq__ = __eq__
print(Container.__eq__)

# Runtime error vs syntax error
# Syntax errors are impossible to be correct and will prevent execution
# Runtime errors deal with incorrect data found during runtime

from random import randint as r # atribbute function to variable
print(r(0, 12)) #inclusive #inclusive


def fib(count):
  a, b = 0, 1
  while count:
    yield a
    a, b, = b, b + a
    count -= 1

gen = fib(100)
print(next(gen), next(gen), next(gen), next(gen), next(gen))

for i in fib(20):
  print(i, end=" ")

# 0 1 1 2 3
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181

#inf = (float('inf')) #other way without math.
print(math.inf)

def fib():
  a, b = 0, 1
  while True:
    yield a
    a, b, = b, b + a

print(list(itertools.islice(fib(), 20)))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

names = ['Caleb', 'Corey', 'Chris', 'Samantha']
points = [100, 250, 30, 600]
zipped = list(zip(names, points))
print(zipped)
# [('Caleb', 100), ('Corey', 250), ('Chris', 30), ('Samantha', 600)]
data = [list(item) for item in zipped]
print(data)
# [['Caleb', 100], ['Corey', 250], ['Chris', 30], ['Samantha', 600]]

names = ['Caleb', 'Corey', 'Chris', 'Samantha', "Hannah", "Kelly"]
points = [100, 250, 30, 600]
zipped = list(zip_longest(names, points))
print(zipped)
# [('Caleb', 100), ('Corey', 250), ('Chris', 30), ('Samantha', 600), ('Hannah', None), ('Kelly', None)]


def zip_lists(list1=[], list2=[], longest=True):
  if longest:
    return [list(item) for item in zip_longest(list1, list2)]
  else:
    return [list(item) for item in zip(list1, list2)]

names = ['Caleb', 'Corey', 'Chris', 'Samantha', "Hannah", "Kelly"]
points = [100, 250, 30, 600]
print(zip_lists(names, points))
# [['Caleb', 100], ['Corey', 250], ['Chris', 30], ['Samantha', 600], ['Hannah', None], ['Kelly', None]]

print(python_version())
# 3.9.8

x = set()
y = {1, 2, 3, 4, 4} # set # {1, 2, 3, 4}
z = {} # dict
y.add(5)
y.remove(1)
y = {2, 3, 4, 5}
w = [2, 3, 4, 5]
print(2 in y) # faster
print(2 in w) # lowest
# y.union()
# y.intersection()
# y.difference()

del fruits['avocado']
print(list(fruits.keys()))
print(list(fruits.values()))

w = [i for i in range(100) if i % 5 == 0] # list
x = {i for i in range(100) if i % 5 == 0} # set
y = {i:0 for i in range(100) if i % 5 == 0} # dictionary
z = (i for i in range(100) if i % 5 == 0) # generated
z = tuple(i for i in range(100) if i % 5 == 0) # tuple

def func(*args, **kwargs):
  print(args, kwargs)

func(1, 2, 3, 4, 5, one=1, two=2)

# scopes and global
x = 'pep' # global
def func(name):
  x = name # local

x = 'pep' # global
def func(name):
  global x
  x = name # global... never use

try:
  x = 7 / 0
except Exception as e:
  print(e)
finally:
  print('done')

x = [1, 2, 23, 54, 123, 56, 324, 34, 6]
mp = map(lambda i: i + 2, x)
print(list(mp))  # [3, 4, 25, 56, 125, 58, 326, 36, 8]
mp = filter(lambda i: i % 4 == 0, x)
print(list(mp))  # [56, 324]
