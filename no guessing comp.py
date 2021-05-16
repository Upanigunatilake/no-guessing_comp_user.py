print("LET'S PLAY GUESS THE SECRET NUMBER")
print('START')
import random
def guess(x):
    random_no=random.randint(1,x)
    guess=0
    while guess!=random_no:
        guess=int(input(f'guess a number between 1 and {x}: '))
        if guess < random_no:
            print('sorry to low. Try again.....')
        elif guess > random_no:
            print('sorry to high. Try again.....')
    print("yay you guessed the correct number..." +str(x)+ '.')
guess(10)


