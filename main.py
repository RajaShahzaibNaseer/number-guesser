#to-do list
# make the menu appear to highlight choices (done)
# add choice functionality 
# add number generator
# add game loop

def menu():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    print("\nPlease select the difficulty level")
    print("1.Easy (10 chances) \n 2. Medium (5 chances) \n 3.Hard (3 chances)")
    print("\n Enter your choice: ")

def main():
    number_to_guess = 1
    game_loop = True
    difficulty = 0
    while game_loop:
        menu()
        choice = input("Enter your choice: ")
        if choice == 1:
            difficulty = 10
        elif choice = 2:
            difficulty = 5
        else:
            difficulty = 3

        while difficulty:
            guess = input("enter your guess")
            if guess == number_to_guess:
                




