print('Hello World!')

num = int(input())

print(3 + 2) # 5    +=
print(3 - 2) # 1    -=
print(3 * 2) # 6    *=
print(3 / 2) # 1.5  /=
print(2 / 2) # 1.0
print(2**3)  # 8
print(7 // 2)# 3
print(7 % 2) # 1

print('uma')
print("duas")
print('''uma
duas
tres linhas''')
print(f'interpolado {num}')

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

len(squares) # 10
squares.append(100) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
squares.insert(0,'fon') # ['fon', 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
squares.index(9) # 4

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
  main()
  _ = 'dont use me!'

import time
import traceback

# while True:
#   try:
#     print('Vrummmmmmm')
#     time.sleep(0.1)
#     raise Exception('que')
#   except Exception:
#     print('unheeeee')

try:
  raise Exception('unheeee')
except Exception as e:
  print(e)
  traceback.print_exc()
  print(traceback.format_exc)

print('ALWAYS MAKE LISTS AS SETs OR HASH TABLES')

def fun(str, arr=None):
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
)

add: lambda x,y: x + y # lambda function

# more_than_one_nums = filter(lambda x: x > 1, [1, 2, 3])
# print(more_than_one_nums)

condition = True
x = 1 if condition else 0
# ternary

num1 = 10_000_000_000
num2 = 100_000_000
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

# help(module_name)

from datetime import datetime
dir(datetime)
datetime.today
datetime.today()
