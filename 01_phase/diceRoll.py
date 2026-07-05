import random

def roll_die():
    return random.randint(1,6)


def main():
    print("welcome to the dice roller!")

    while True:
        user_input = input("press 'r' to roll the die or 'e' to exit: ")
        if user_input.lower() == 'e':
            break
        elif user_input.lower()== 'r':
            result =roll_die()
            print(f"You rolled a {result}!")
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()