#SECTION 2: Trip Planner Answer

#write code for hotel_cost()
def hotel_cost(nights):
    '''calculates the cost for a hotel room'''
    cost = nights * 140

    if (nights > 5):
        cost = cost - (cost * 0.10)

    return cost

#write code for plane_cost()
def plane_cost(city):
    '''returns the cost of a round trip ticket'''
    if (city == "Charlotte"):
        return 183
    elif (city == "New York City"):
        return 362
    elif (city == "Los Angeles"):
        return 320
    elif (city == "Tampa"):
        return 252
    elif (city == "Philadelphia"):
        return 260
    elif (city == "Boston"):
        return 304
    elif (city == "Houston"):
        return 248
    elif (city == "Seattle"):
        return 191

#write code for rental_cost()
def rental_cost(days):
    '''calculates the cost of a rental car'''
    cost = 80

    for i in range(1, days):
        cost += 40

    if (days >= 7):
        cost -= 50
    elif (days >= 3):
        cost -= 30
        
    return cost

#add code for calculate_trip_cost()
def calculate_trip_cost(city, days, nights):
    '''calculates the cost of a total trip'''
    hotel = hotel_cost(nights)
    plane = plane_cost(city)
    car = rental_cost(days)
    
    return int(hotel + plane + car)

def main():
    city = input("Where are you traveling?: ")
    days = int(input("How many days will you be staying?: "))
    nights = int(input("How many nights will you be spending?: "))
    print("Your trip will cost ${}.".format(calculate_trip_cost(city, days, nights)))
    
##    #TESTING -- UNCOMMENT TO TEST
##    print("$" + str(calculate_trip_cost("Los Angeles", 3, 3))) #should return $870
##    print("$" + str(calculate_trip_cost("New York City", 6, 5))) #should return $1312
##    print("$" + str(calculate_trip_cost("Philadelphia", 5, 5))) #should return $1170
##    print("$" + str(calculate_trip_cost("Houston", 2, 3))) #should return $788
##    print("$" + str(calculate_trip_cost("Seattle", 8, 7))) #should return $1383


if __name__ == "__main__":
    main()
