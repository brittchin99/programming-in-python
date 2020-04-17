#PROJECT: Mad Libs
#INSTRUCTIONS - create a Mad Libs story where a user will enter multiple words
#which will then be placed into a story

#define the variables you want to use in your story
place = input("Enter a place: ")
adj1 = input("Enter an adjective: ")
animal = input("Enter an animal: ")
color = input("Enter a color: ")
fruit = input("Enter a fruit: ")
adj2 = input("Enter another adjective: ")
verb = input("Enter an action verb (past tense): ")

#print your story here
print("I was walking through the {} when I saw a {} {}.".format(place, adj1, animal))
print("The {} was eating a {} {}.".format(animal, color, fruit))
print("I asked the {} where he got the {}, but he yelled".format(animal, fruit))
print('"Go away you {} human"!'.format(adj2))
print("He threw the {} at me, so I quickly {} away.".format(fruit, verb))
