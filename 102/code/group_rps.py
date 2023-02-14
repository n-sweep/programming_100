import random

d = {'rock':'scissors','paper':'rock','scissors':'paper'}

user1 = input("Would you like to play Rock, Paper, Scissors? ")

if user1 == "yes":
  userRes = input("Rock, Paper, or Scissors? \n").lower()
  r = random.choice(list(d.keys()))

  print("Computer chose",r)

  if d[userRes] == r:
    print("You've won!")

  elif d[r] == userRes:
    print("You've lost.")

  else:
    print("Tie, try again")
