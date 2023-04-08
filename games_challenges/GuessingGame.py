#############################################
#### Guessing Game Challenge - Solution #####
#############################################

"""
Write a program that picks a random integer from 1 to 100, 
and has players guess the number. The rules are:

1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"

2. On a player's first turn, if their guess is
--- within 10 of the number, return "WARM!"
--- further than 10 away from the number, return "COLD!"

3. On all subsequent turns, 
- if a guess is closer to the number than the previous guess return "WARMER!". 

- if farther from the number than the previous guess, return "COLDER!"

4. When the player's guess equals the number, tell them they've guessed correctly 
and how many guesses it took!
"""

import random as r
computer = r.randint(1,100)

print('Guessing Game', computer)
player = 0
guessList = [0]

while player != computer:
    
    player = int(input('What is your number?'))
    if player < 1 or player > 100: 
        print('OUT')
        continue
    elif player == computer:
        print(f'CONGRATS, YOU TRY {len(guessList)} TIMES.')
        break
    
    guessList.append(player)

    if guessList[-2] != 0:
        if guessList.count(player) > 1:
            print('SAME NUMBER')
        elif abs(computer - player) < abs(computer - guessList[-2]):
            print('CLOSER')
        else:
            print('FARTHER')
    else:
        if abs(player - computer) <= 10:
            print('CLOSE')
        else:
            print('FAR')
    
    
