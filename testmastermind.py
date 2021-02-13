#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 13:11:39 2018
@author: andinabaca
"""

import random

c = 5       #number of colours
m = 4       #number of positions
a = 1       #the number of the current position 

print('==========================\n{:^26s}\n=========================='\
      .format('Welcome to Mastermind!'))
print('Choose {} numbers between 0 and'.format(m), c)
print('\nBlack Score equals correct number in the correct place \nWhite Score equals correct number but in wrong place\n')
print('\nRound 0:')

L1 = [random.randint(0, c) for i in range(m)] #codemaker code
#print(L1)

  
rounds = 10       #number of rounds to play the game

collectscore = []     

def game(L1,m,a):
    L2 = []
    for i in range(m):
        x = (input('Enter color for position {}: '.format(a)))
        if not x.isdigit() or (int(x)<0 or int(x)>c):
            return -1
        a += 1
        L2.append(int(x))
    black = 0
    white = 0
    black = sum([1 if i == j else 0 for i,j in zip(L2,L1)]) #If integer is same at same index, adds to black
    temp = L1[:]
    for q in L2:
        if q in temp:
            white+=1
            temp.remove(q)
    white -= black
    total = (L2, black, white)
    collectscore.append(total)
    print('\n=============== Game Board ===============\n')
    for x in collectscore:
        print(x[0],'\tScore: ','Black = ', x[1],'White = ',x[2])
    return black 

    
for attempt in range(rounds):
    output = game(L1,m,a)
    if output == m:
        print('\n=============== Game Board ===============\n')
        print('Congrats! You have won!\nThe secret code is: ',L1)
        break
    if output == -1:
        print('INPUT ERROR: Game terminated\nThe secret code is: ',L1)
        break
    else:
        print('\nRound {}:'.format(0 +1+ attempt))
else:
    print('\n=============== Game Board ===============\n')
    print('Game terminated\nThe secret code was: ',L1)



    