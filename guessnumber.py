import random
print('game guess the number, you only have 3 shots!')

n = input('enter your name:')
s = random.randint(1,10)
t = 0

if t == 0:
    a = int(input(f'Hey {n} guess the number:'))
    t +=1

if a > s:
    print("lower")

if a < s:
    print('higher')

while a!=s and t<3:
    a = int(input("try again:"))
    t+=1
    if a > s:
        print("lower")
    if a < s:
        print('higher')

if a == s:
    print(f'Nice shot {n}! \n tries:{t}')
else:
    print(f'{n} you have no attempts remain\nGAME OVER')


