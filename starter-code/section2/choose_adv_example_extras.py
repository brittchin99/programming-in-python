#PROJECT: Choose Your Own Adventure
#INSTRUCTIONS - create a Choose Your Own Adventure Game where
#players will make choices that lead to different outcomes
import random

def play_again():
    '''asks the user if they want to play again, returns True if they do'''
    again = input("Would you like to play again? (Y)ES or (N)O: ")
    again = again.upper().strip()

    while again != "YES" and again != "Y" and again != "NO" and again != "N":
        print("Invalid response.")
        again = input("Would you like to play again? (Y)ES or (N)O: ")
        again = again.upper().strip()

    print()

    if (again in "YES"):
        return True
    else:
        return False
    
def validate_input(question, option1, option2):
    '''validates the user input'''
    guess = input(question)
    guess = guess.upper().strip()
    
    while (guess != option1 and guess != option2):
        print("Invalid response.")
        guess = input(question)
        guess = guess.upper().strip()
    
    return guess

def print_intro():
    '''prints the introduction to the game'''
    print("Welcome to Nightmare, a game where your actions have consequences.")
    print("Will you survive to the end of the night?")
    print()
    
def play_game():
    '''plays the game'''
    
    print_intro()
    print("You're lying on your bed in the middle of the night.")
    print("Suddenly, you hear a noise downstairs. You look at your clock. It's 3 A.M.")
    user_answer = validate_input("Do you INVESTIGATE or HIDE?: ", "INVESTIGATE", "HIDE")

    if user_answer == "INVESTIGATE":
        print ("You leave your room and walk to the stairs.")
        user_answer = validate_input("Do you go to the KITCHEN or the LIVING ROOM?: ", "KITCHEN", "LIVING ROOM")

        if user_answer == "KITCHEN":
            print ("You walk into the kitchen and try to turn on the light. The power is out.")
            user_answer = validate_input("Do you grab a KNIFE or a FRYING PAN?: ", "KNIFE", "FRYING PAN")

            if user_answer == "KNIFE":
                print ("You take a knife from the drawer and head to the basement.")
                print ("You reach the basement and hear a growl behind you. It's the monster!")
                user_answer = validate_input("Do you FIGHT or RUN?: ", "FIGHT", "RUN")

                if user_answer == "FIGHT":
                    print ("You fight the monster and stab him in the stomach. You are a hero!")
                else:
                    print ("You try to run away from the monster, but you trip. The last thing you see is glowing eyes right behind you.")
                    print ("GAME OVER")
            else:
                print ("You grab the frying pan off the counter and head to the basement.")
                print ("On the way to the basement, you trip down the stairs and hit yourself with the frying pan.")
                print ("GAME OVER.")
        else:
            print ("You walk into the living room and try to turn on the light. The power is out.")
            user_answer = validate_input("Do you grab a FLASHLIGHT or RUN out the front door?: ", "FLASHLIGHT", "RUN")

            if user_answer == "FLASHLIGHT":
                print ("You take the flash light and head to the basement.")
                print ("You reach the basement and hear a growl behind you. It's the monster!")
                user_answer = validate_input("Do you FIGHT or RUN?: ", "FIGHT", "RUN")

                if user_answer == "FIGHT":
                    print ("You try to fight the monster with the flash light. He knocks you in the head and you pass out. When you wake up, you realize it was all a nightmare.")
                else:
                    print ("You try to run away from the monster, but you trip. The last thing you see is glowing eyes right behind you.")
                    print ("GAME OVER.")
            else:
                print ("You run to the front door, open it, and sprint out of the house. Unlucky for you, you don't see the car coming around the corner.")
                print ("GAME OVER.")
    else:
        print ("You choose to stay in your room.")
        user_answer = validate_input("Do you hide under your BED or in your CLOSET?: ", "BED", "CLOSET")

        if user_answer == "BED":
            print ("You crawl under your bed and wait. You don't hear any more noises and you're safe. Suddenly something grabs your feet and drags you out. You black out.")
            print ("GAME OVER")
        else:
            print ("You choose to hide in your closet. You wait anxiously.")
            user_answer = validate_input("Do you continue WAITING or PEEK out?: ", "WAITING", "PEEK")

            if user_answer == "WAITING":
                print ("You wait a few more minutes until it's safe to come out.")
                print ("You leave your room and walk to the stairs.")
                user_answer = validate_input("Do you go to the KITCHEN or the LIVING ROOM?: ", "KITCHEN", "LIVING ROOM")

                if user_answer == "KITCHEN":
                    print ("You walk into the kitchen and try to turn on the light. The power is out.")
                    user_answer = validate_input("Do you grab a KNIFE or a FRYING PAN?: ", "KNIFE", "FRYING PAN")

                    if user_answer == "KNIFE":
                        print ("You take a knife from the drawer and head to the basement.")
                        print ("You reach the basement and hear a growl behind you. It's the monster!")
                        user_answer = validate_input("Do you FIGHT or RUN?: ", "FIGHT", "RUN")

                        if user_answer == "FIGHT":
                            print ("You fight the monster and stab him in the stomach. You are a hero!")
                        else:
                            print ("You try to run away from the monster, but you trip. The last thing you see is glowing eyes right behind you.")
                            print ("GAME OVER")
                    else:
                        print ("You grab the frying pan off the counter and head to the basement.")
                        print ("On the way to the basement, you trip down the stairs and hit yourself with the frying pan.")
                        print ("GAME OVER.")
                else:
                    print ("You walk into the living room and try to turn on the light. The power is out.")
                    user_answer = validate_input("Do you grab a FLASHLIGHT or RUN out the front door?: ", "FLASHLIGHT", "RUN")

                    if user_answer == "FLASHLIGHT":
                        print ("You take the flash light and head to the basement.")
                        print ("You reach the basement and hear a growl behind you. It's the monster!")
                        user_answer = validate_input("Do you FIGHT or RUN?: ", "FIGHT", "RUN")

                        if user_answer == "FIGHT":
                            print ("You try to fight the monster with the flash light. He knocks you in the head and you pass out. When you wake up, you realize it was all a nightmare.")
                        else:
                            print ("You try to run away from the monster, but you trip. The last thing you see is glowing eyes right behind you.")
                            print ("GAME OVER")
                    else:
                        print ("You run to the front door, open it, and sprint out of the house. Unlucky for you, you don't see the car coming around the corner.")
                        print ("GAME OVER.")
            else:
                print ("You peek out of the closet. You think it's safe. Suddenly you hear a growl, and the last thing you see before you black out is a pair of glowing red eyes.")
                print ("GAME OVER.")

    print()

def main():
    ''''''
    done = False

    while(not done):
        play_game()

        again = play_again()

        if (not again):
            print("Thanks for playing!")
            done = True
        
if __name__ == "__main__":
    main()
