# a little magic 8-ball program

from random import choice

answers = [
    "It is certain.", "It is decidedly so.", "Without a doubt.",
    "Yes definitely.", "You may rely on it.", "As I see it, yes.",
    "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
    "Reply hazy, try again.", "Ask again later.",
    "Better not tell you now.", "Cannot predict now.",
    "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
    "My sources say no.", "Outlook not so good.", "Very doubtful."
]

while True:  # loop until `break` statement is called

    # get a response from the user, give them the option to quit
    response = input('Ask a yes/no question: (q to quit)\n')

    # if the user chooses to quit, break the loop
    if response.lower() == 'q':
        break

    # randomly choose an anser & print
    else:
        answer = choice(answers)
        print(answer, '\n')
