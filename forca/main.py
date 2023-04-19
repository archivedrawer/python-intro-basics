from random import choice
import os
import re

with open('banco') as file:
  data = file.read()

banco = data.splitlines()

hidden = choice(banco)

word = ['_' for l in hidden]

letters = []

tries = 0

wrong = []

while True:
  os.system('clear')
  print(f'Tries: {tries}.', f'Wrong: {"-".join(wrong)}')
  print(' '.join(word))

  if ''.join(word) == hidden:
    print('You won!')
    break

  if tries == 5:
    print(f'You lost. The word was {hidden}.')
    break

  while True:
    letter = input('Choose one letter: ')[:1].lower()
    if letter not in letters:
      letters.append(letter)
      break

  match = [m.start() for m in re.finditer(letter, hidden)]
  if match:
    for i in match:
      word[i] = letter
  else:
    wrong.append(letter)
    tries += 1