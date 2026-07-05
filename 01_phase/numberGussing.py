import random

secrect_number = random.randint(1,5)


while True:
    user_input  = input("Guess the no between 1 to 5: ")

    if user_input.isdigit():
        user_input = int(user_input)
        if user_input == secrect_number:
            print("You guessed it right!")
            break
        else:
            print("try again")
            




