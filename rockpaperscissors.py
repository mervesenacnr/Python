import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

choose_A = rock, paper, scissors
choose_B = rock, paper, scissors

A = random.choice(choose_A)
B = random.choice(choose_B)

print('Person A', A)
print('Person B', B)

if A == B:
    print('Draw')
elif A == rock and B == scissors:
    print('Person A wins')
elif A == rock and B == paper:
    print('Person B wins')
elif A == paper and B == scissors:
    print('Person B wins')
elif A == paper and B == rock:
    print('Person A wins')
elif A == scissors and B == rock:
    print('Person B wins')
elif A == scissors and B == paper:
    print('Person A wins')

