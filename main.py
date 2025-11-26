#to-do list
# make the menu appear to highlight choices (done)
# add choice functionality (done) 
# add number generator (done)
# add game loop (done)
# fix difficulty not being chosen correctly
# fix menu layout
# add game end state
# add game quit option
# fix compare_numbers not working (done)
#

import random


def menu():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    print("\nPlease select the difficulty level")
    print("1.Easy (10 chances) \n2.Medium (5 chances) \n3.Hard (3 chances) \n4.Quit")

def main():
    number_to_guess = random.randint(0, 100)
    print(number_to_guess)
    game_loop = True
    difficulty = 0
    while game_loop:
        menu()
        choice = input("Enter your choice: ")
        print(choice)
        
        if choice == "1":
            difficulty = 10
        elif choice == "2":
            difficulty = 5
        elif choice == "3":
            difficulty = 3
        elif choice == "4":
            game_loop == False
            break
        print(difficulty)
        while difficulty != 0:
            guess = input("enter your guess: ")
            if int(guess) == int(number_to_guess):
                game_loop = False
                difficulty = 0
                print("you win!")
            else:
                compare_numbers = lambda x : f"number is greater then {x}" if int(x) < number_to_guess else f"number is less then {x}"
                print(f"You guessed wrong!{compare_numbers(guess)}")
                print(f"you have {difficulty} guesses remaining")
                difficulty -= 1

if __name__ == "__main__":
    main()


