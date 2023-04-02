import random

print('ROCK ------PAPER-------SCISSIORS')
print('\t\tCHOOSE ONE')

compu = random.randint(1, 3)
print('The computer has locked its answer')
if compu == 1:
  compu = 'rock'
elif compu == 2:
  compu = 'paper'
else:
  compu = 'scissiors'


userr = input("Write you option here: ")
userr = userr.lower()
# print(userr)
if userr == compu:
  print('TIED')
  print(f'YOU CHOOSE:{userr}')
  print(f'COMPUTER CHOOSE:{compu}')

if userr == 'rock' and compu == 'paper':
  print('YOU LOST')
  print(f'YOU CHOOSE:{userr}')
  print(f'COMPUTER CHOOSE:{compu}')
elif userr == 'paper' and compu == 'rock':
  print('YOU WON')
  print(f'YOU CHOOSE:{userr}')
  print(f'COMPUTER CHOOSE:{compu}')
elif userr == 'rock' and compu == 'scissiors':
  print('YOU WON')
  print(f'YOU CHOOSE:{userr}')
  print(f'COMPUTER CHOOSE:{compu}')
elif userr == 'scissiors' and compu == 'rock':
  print('YOU LOST')
  print(f'YOU CHOOSE:{userr}')
  print(f'COMPUTER CHOOSE:{compu}')
elif userr == 'paper' and compu == 'scissiors':
  print('YOU WON')
  print(f'YOU CHOOSE:{userr}')
  print(f'COMPUTER CHOOSE:{compu}')
elif userr == 'scissiors' and compu == 'paper':
  print('YOU WON')
  print(f'YOU CHOOSE:{userr}')
  print(f'COMPUTER CHOOSE:{compu}')
  
