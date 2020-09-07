#PROJECT: Guess the Number - NO LISTS
#INSTRUCTIONS - create a Guess the number game, where users will try and
#guess a random number generated from the computer
import random


def print_intro(start, end):
    '''prints the introduction to the game'''
    print("Welcome to Guess the Number!")
    print("Try and guess the secret number from {} to {}.".format(start, end))
    
def play_game():
    '''plays the game until the user guesses the number'''
    #generate and store the random number to guess in the range start and end
    start = 1
    end = 20
    num_to_guess = random.randint(start, end)

    #keep a var for if the number was guessed
    guessed = False

    print_intro(start, end)

    while(not guessed): #while the number is not guessed
        print()
        
        guess = input("Guess the number: ")
        guess = int(guess)

        if (guess == num_to_guess): #if the user guesses the number
            print("You guessed the number!")
            guessed = True

        elif (guess > num_to_guess): #if the guess is too high
           print("You guessed too high, try again!")
           
        else: #if the guess is too low
            print("You guessed too low, try again!")


def main():
    ''''''
    play_game()
        
if __name__ == "__main__":
    main()
