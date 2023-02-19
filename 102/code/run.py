# a very minimal 'rock, paper, scissors' game

from random import choice

results = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['paper', 'spock'],
    'spock': ['rock', 'scissors']
}

user_choice = input('RPSLS?')
comp_choice = choice(list(results.keys()))

print(comp_choice)
# tie
if user_choice == comp_choice:
    print("it's a tie")
# win
elif comp_choice in results[user_choice]:
    print('you won!')
# lose
else:
    print('you lose.')
