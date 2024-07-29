i = 1
while i <= 5:
    print(i)
    i += 1
print("Done")

#e.g. guessing game
secret_number = rand()
guess_count = 0
guess_max = 3
while guess_count < guess_max:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("Correct!!!")
        break
else:
    print("You lose.. .Bitchhh")

#guessing game 2 (concept)
import random

# Set the range for the random number
lower_bound = 1
upper_bound = 100

# Generate a random number
number_to_guess = random.randint(lower_bound, upper_bound)

# Welcome message
print(f"Welcome to the Guessing Game! Try to guess the number between {lower_bound} and {upper_bound}.")

# Initialize the number of attempts
attempts = 0

# Game loop
while True:
    # Increment the attempt counter
    attempts += 1

    # Get the player's guess
    guess = int(input("Enter your guess: "))

    # Check if the guess is correct
    if guess == number_to_guess:
        print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts.")
        break
    elif guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

#Car Game
#My code:
input1 = ""
while True:
    input1 = input(">").lower()
    if input1 == "help":
        print(
        """
start - to start the car
stop - to stop the car
quit - to exit
        """)
        break
    else:
        print("I don't understand that.")

def game():
    input2 = ""
    last_action = ""
    while True:
        input2 = input(">").lower()
        if input2 == "start":
            if last_action == "start":
                print("The car already moving.")
            else:
                print("Car started...Ready to go!")
                last_action = "start"
        elif input2 == "stop":
            if last_action == "stop":
                print("The car already stopped.")
            else:
                print("Car stopped.")
                last_action = "stop"
        elif input2 == "quit":
            print("Game exited.")
            return
        else:
            print("Invalid input. Try again.")

game()

#My tutor code:
command = ""
started = False
while True :
    command = input("> ").lower()
    if command == "start":
        if started:
            print("The car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("The car is already stopped!!")
        else:
            started = False
            print("The car is stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit -  to exit
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand that.")

