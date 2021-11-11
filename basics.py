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