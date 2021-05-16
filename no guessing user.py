print('LET US PLAY A NEW GAME.JUST THINK OF A NUMBER BETWEEN 1 AND 1000 AND I WILL GUESS THE NUMBER YOU THOUGHT')
print(' ARE YOU READY WITH A NUMBER?')
print('START')

import random
def comp_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if low!=high:
            guess = random.randint(low,high)
        else:
            guess =low  #could also be high cuz low=high
        feedback=input(f'IS {guess} high(H),low (L), correct(C).').lower()
        if feedback=='h':
            high= guess-1
        elif feedback=='l':
            low= guess+1

    print(f'yay... I guessed the number {guess} correctly')
comp_guess(1000)