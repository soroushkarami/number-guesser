import random
chosen = random.choice(range(1,11))
while True:
    try:
        user = int(input('Your Guess: '))
    except ValueError:
        print('Enter a number please!')
        raise
    if user == chosen:
        print('Congrats!!')
        break
    elif user > chosen:
        print('You are too high!')
    elif user < chosen:
        print('You are too low!')