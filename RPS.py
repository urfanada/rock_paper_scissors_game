import random

choices = ['rock', 'paper', 'scissors']

while True:
    user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ")

    if user_choice == 'exit':
        break

    if user_choice not in choices:
        print("Invalid input, please choose rock, paper, or scissors.")
        continue

    computers_choice = random.choice(choices)
    print(f"Computer chose: {computers_choice}")

    if user_choice == computers_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computers_choice == 'scissors') or \
         (user_choice == 'paper' and computers_choice == 'rock') or \
         (user_choice == 'scissors' and computers_choice == 'paper'):
        print("You win!")
    else:
        print("You lose!")
