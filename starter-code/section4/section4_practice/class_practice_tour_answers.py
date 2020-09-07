#PRACTICE: Tour and Tour Guide

class Tour():

    #every tour should be instantiated with a title, description, location, and guide
    def __init__(self, title, description, location, guide):
        self.title = title
        self.description = description
        self.location = location
        self.guide = guide

    def getTourInfo(self):
        '''prints the title, decription, location, and guide name for the tour'''
        print("Tour name:", self.title)
        print("Led by {} {}".format(self.guide.firstName, self.guide.lastName))
        print("Location:", self.location)
        print("Description:", self.description)


class Guide():

    def __init__(self, firstName, lastName):
        '''every guide should have a first name, last name, and list of tours
            the only parameters passed in should be first and last name
            their tour list should be instantiated as an empty list'''
        self.firstName = firstName
        self.lastName = lastName
        self.tours = []

    def getGuideInfo(self):
        '''prints the first name, last name, and list of tours for the guide'''
        print("Name: {} {}".format(self.firstName, self.lastName))
        print("Tours:", self.tours)

    def addTour(self, title, description, location):
        '''instantiates a new tour and adds it to the guide's tour list
            the only parameters should be title, description, and location'''
        tour = Tour(title, description, location, self)
        self.tours.append(tour)

    def getTours(self):
        '''returns the guide's tours'''
        return self.tours

def main():

    guide1 = Guide("Emily", "Gonzalez")
    guide2 = Guide("Tommy", "Brown")
    
    guide1.getGuideInfo() #Name: Emily Gonzalez Tours: []
    guide2.getGuideInfo() #Name: Tommy Brown Tours: []

    guide1.addTour("Food and Wine Tour", "A day long tour visiting 6 food places.", "Paris, France")
    guide2.addTour("Carriage Tour of Boston", "Horse and carriage tour of the city.", "Boston, Massachusetts")
    guide2.addTour("The Monuments at Night", "A private tour of the most popular monuments lit up at night.", "Washington D.C.")

    guide1.getGuideInfo() #Name: Emily Gonzalez Tours: [<__main__.Tour object at [some location in memory]>]
    guide2.getGuideInfo() #Name: Tommy Brown Tours: [<__main__.Tour object at [some location in memory]>, <__main__.Tour object at [some location in memory]>]

    for tour in guide1.getTours():
        tour.getTourInfo()

    #Tour name: Food and Wine Tour
    #Led by Emily Gonzalez
    #Location: Paris, France
    #Description: A day long tour visiting 6 food places.

    for tour in guide2.getTours():
        tour.getTourInfo()

    #Tour name: Carriage Tour of Boston
    #Led by Tommy Brown
    #Location: Boston, Massachusetts
    #Description: Horse and carriage tour of the city.
        
    #Tour name: The Monuments at Night
    #Led by Tommy Brown
    #Location: Washington D.C.
    #Description: A private tour of the most popular monuments lit up at night.

if __name__ == "__main__":
    main()
