#PROJECT: Choose Your Own Adventure
#INSTRUCTIONS - create a Choose Your Own Adventure Game where
#players will make choices that lead to different outcomes

def print_intro():
    '''prints the introduction to the game'''
    print("Welcome to Nightmare, a game where your actions have consequences.")
    print("Please type your answers in ALL CAPS.")
    print()
    
def play_game():
    '''plays the game'''
    
    print()

    print_intro()
    
    print ("You're lying on your bed in the middle of the night. Suddenly, you hear a noise downstairs. You look at your clock. It's 3 A.M.")
    choice1 = input ("Do you INVESTIGATE or HIDE? ")

    if choice1 == "INVESTIGATE":
        print ("You leave your room and walk to the stairs.")
        choice2 = input ("Do you go to the KITCHEN or the LIVING ROOM? ")

        if choice2 == "KITCHEN":
            print ("You walk into the kitchen and try to turn on the light. The power is out.")
            choice3 = input ("Do you grab a KNIFE or a FRYING PAN? ")

            if choice3 == "KNIFE":
                print ("You take a knife from the drawer and head to the basement.")
                print ("You reach the basement and hear a growl behind you. It's the monster!")
                choice4 = input ("Do you FIGHT or RUN? ")

                if choice4 == "FIGHT":
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
            choice3 = input ("Do you grab a FLASHLIGHT or RUN out the front door? ")

            if choice3 == "FLASHLIGHT":
                print ("You take the flash light and head to the basement.")
                print ("You reach the basement and hear a growl behind you. It's the monster!")
                choice4 = input ("Do you FIGHT or RUN? ")

                if choice4 == "FIGHT":
                    print ("You try to fight the monster with the flash light. He knocks you in the head and you pass out. When you wake up, you realize it was all a nightmare.")
                else:
                    print ("You try to run away from the monster, but you trip. The last thing you see is glowing eyes right behind you.")
                    print ("GAME OVER.")
            else:
                print ("You run to the front door, open it, and sprint out of the house. Unlucky for you, you don't see the car coming around the corner.")
                print ("GAME OVER.")
    else:
        print ("You choose to stay in your room.")
        choice2 = input ("Do you hide under your BED or in your CLOSET? ")

        if choice2 == "BED":
            print ("You crawl under your bed and wait. You don't hear any more noises and you're safe. Suddenly something grabs your feet and drags you out. You black out.")
            print ("GAME OVER")
        else:
            print ("You choose to hide in your closet. You wait anxiously.")
            choice3 = input ("Do you continue WAITING or PEEK out? ")

            if choice3 == "WAITING":
                print ("You wait a few more minutes until it's safe to come out.")
                print ("You leave your room and walk to the stairs.")
                choice4 = input ("Do you go to the KITCHEN or the LIVING ROOM? ")

                if choice4 == "KITCHEN":
                    print ("You walk into the kitchen and try to turn on the light. The power is out.")
                    choice5 = input ("Do you grab a KNIFE or a FRYING PAN? ")

                    if choice5 == "KNIFE":
                        print ("You take a knife from the drawer and head to the basement.")
                        print ("You reach the basement and hear a growl behind you. It's the monster!")
                        choice6 = input ("Do you FIGHT or RUN? ")

                        if choice6 == "FIGHT":
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
                    choice3 = input ("Do you grab a FLASHLIGHT or RUN out the front door? ")

                    if choice3 == "FLASHLIGHT":
                        print ("You take the flash light and head to the basement.")
                        print ("You reach the basement and hear a growl behind you. It's the monster!")
                        choice4 = input ("Do you FIGHT or RUN ?")

                        if choice4 == "FIGHT":
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

def main():
    play_game()

if __name__ == "__main__":
    main()
