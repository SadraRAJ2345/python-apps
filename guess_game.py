import random

system_number = random.randint(1,4)

for i in range(3):
    user_input = int(input("Enter Your guessed number: "))
    if user_input == system_number:
        print("You won the game.")
        break
    else:
        continue