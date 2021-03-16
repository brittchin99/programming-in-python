#PRACTICE: Tour and Tour Guide
#Instructions: complete the methods for the given classes

class Tour():

    #every tour should be instantiated with a title, description, location, and guide
    def __init__(self):
        pass #remove thie once you write code

    def getTourInfo(self):
        '''prints the title, decription, location, and guide name for the tour'''
        pass #remove thie once you write code
    
        #Tour name: ""
        #Led by ""
        #Location: ""
        #Description: ""
        
class Guide():

    def __init__(self, firstName, lastName):
        '''every guide should have a first name, last name, and list of tours
            the only parameters passed in should be first and last name
            their tour list should be instantiated as an empty list'''
        pass #remove thie once you write code

    def getGuideInfo(self):
        '''prints the first name, last name, and list of tours for the guide'''
        pass #remove thie once you write code
        
        #Name: ""
        #Tours: []
    
    def addTour(self, title, description, location):
        '''instantiates a new tour and adds it to the guide's tour list
            the only parameters should be title, description, and location'''
        pass #remove thie once you write code

    def getTours(self):
        '''returns the guide's tours'''
        pass #remove thie once you write code


def main():
    
##    TESTING: uncomment to test
##    guide1 = Guide("Emily", "Gonzalez")
##    guide2 = Guide("Tommy", "Brown")
##    
##    guide1.getGuideInfo() #Name: Emily Gonzalez Tours: []
##    guide2.getGuideInfo() #Name: Tommy Brown Tours: []
##
##    guide1.addTour("Food and Wine Tour", "A day long tour visiting 6 food places.", "Paris, France")
##    guide2.addTour("Carriage Tour of Boston", "Horse and carriage tour of the city.", "Boston, Massachusetts")
##    guide2.addTour("The Monuments at Night", "A private tour of the most popular monuments lit up at night.", "Washington D.C.")
##
##    guide1.getGuideInfo() #Name: Emily Gonzalez Tours: [<__main__.Tour object at [some location in memory]>]
##    guide2.getGuideInfo() #Name: Tommy Brown Tours: [<__main__.Tour object at [some location in memory]>, <__main__.Tour object at [some location in memory]>]
##
##    for tour in guide1.getTours():
##        tour.getTourInfo()
##
##    #Tour name: Food and Wine Tour
##    #Led by Emily Gonzalez
##    #Location: Paris, France
##    #Description: A day long tour visiting 6 food places.
##
##    for tour in guide2.getTours():
##        tour.getTourInfo()
##
##    #Tour name: Carriage Tour of Boston
##    #Led by Tommy Brown
##    #Location: Boston, Massachusetts
##    #Description: Horse and carriage tour of the city.
##        
##    #Tour name: The Monuments at Night
##    #Led by Tommy Brown
##    #Location: Washington D.C.
##    #Description: A private tour of the most popular monuments lit up at night.

if __name__ == "__main__":
    main()
