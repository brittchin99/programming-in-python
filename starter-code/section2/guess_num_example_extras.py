#PROJECT: Guess the Number - NO LISTS
#INSTRUCTIONS - create a Guess the number game, where users will try and
#guess a random number generated from the computer
import random

def play_again():
    '''asks the user if they want to play again, returns True if they do'''
    again = input("Would you like to play again? (y)es or (n)o?: ")

    while(again != 'yes' and again != 'y' and again != 'no' and again != 'n'):
        print("Invalid response.")
        again = input("Would you like to play again? (y)es or (n)o: ")

    if (again == 'y' or again == 'yes'):
        return True
    else:
        return False

def quit_game():
    '''asks the user if they want to end the game, returns True if they do'''
    end_game = input("Are you sure you want to quit? (y)es or (n)o: ")

    while(end_game != 'yes' and end_game != 'y' and end_game != 'no' and end_game != 'n'):
        print("Invalid response.")
        end_game = input("Are you sure you want to quit? (y)es or (n)o: ")

    if(end_game == 'y' or end_game == 'yes'):
        return True
    else:
        return False
    
def validate_input(guess, start, end, nums_guessed):
    '''validates the user input, returns True if the input is valid'''
    if (guess == 'q'): #if the user wants to quit the game
        if (quit_game()):
            return True
        return False

    if (not guess.isdigit()): #if the guess is not a whole number
        print("Please enter a valid whole number.")
        return False

    elif (guess in nums_guessed): #if the number has already been guessed
        print("You have already guessed this number!")

    elif (int(guess) < start or int(guess) > end): #if the number is not in the range
        print("Please enter a number from {} and {}.".format(start, end))
        return False

    else:
        return True

def print_intro(start, end, guesses):
    '''prints the introduction to the game'''
    print("Welcome to Guess the Number!")
    print("Try and guess the secret number from {} to {}.".format(start, end))
    print("You will have {} guesses.".format(guesses))
    print("Type 'q' at any time to quit the game.")
    
def play_game():
    '''plays the game until the user guesses the number'''
    #generate and store the random number to guess in the range start and end
    start = 1
    end = 20
    num_to_guess = random.randint(start, end)

    #keep a string of guessed numbers, a var for if the number was guessed, a var for guesses left, and guesses made
    nums_guessed = ""
    guessed = False
    guesses = 5
    count = 0

    print_intro(start, end, guesses)

    while(not guessed and guesses > 0): #while the number is not guessed and the user is not out of guesses
        print()
        print("Number of guesses left: {}".format(guesses))

        count += 1
        guess = input("Guess the number: ".format(start, end))
        while (not validate_input(guess, start, end, nums_guessed)):
            guess = input("Guess the number: ".format(start, end))

        if(guess == 'q'): #if the user wants to quit
            print("The number was {}.".format(num_to_guess))
            return False

        nums_guessed += guess
        guess = int(guess)

        if (guess == num_to_guess): #if the user guesses the number
            print("You guessed the number in {} guesses!".format(count))
            guessed = True

        elif (guess > num_to_guess): #if the guess is too high
            guesses -= 1
            
            if (guesses != 0):
                print("You guessed too high, try again!")
            else:
                print("You guessed too high!")
                print("The number was {}.".format(num_to_guess))

        else: #if the guess is too low
            guesses -= 1

            if(guesses != 0):
                print("You guessed too low, try again!")
            else:
                print("You guessed too low!")
                print("The number was {}.".format(num_to_guess))

    print()
    return True

def main():
    ''''''
    done = False

    while(not done):
        user_won = play_game()

        if (not user_won or not play_again()): #if the user quit or does not want to play again
            print("Thanks for playing!")
            done = True

        print()
        
if __name__ == "__main__":
    main()
