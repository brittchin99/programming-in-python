#SECTION 3: Data Structures Practice
#INSTRUCTIONS - write code to finish each function below, then uncomment the tests to check your work

def in_list(L, x):
    '''takes a list L and an int x and returns True if the element x appears in L
    and False if it does not. You CANNOT use the builtin functions 'in' or 'not in' for this problem'''

    for item in L:
        if (item == x):
            return True

    return False

def most_occurances(L):
    '''takes a list L and returns the element that appears the most times.
    Assume the list is not empty and there is a most occurring element.'''
    counts = {}

    for item in L:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    largest = 0
    element = ""

    for key in counts:
        if (counts[key] > largest):
            largest = counts[key]
            element = key
    
    return element

def highest_average(students):
    '''takes a dictionary where the keys are students and the values are lists of grades.
    The function should return the name of the student with the highest average (sum of grades/num of grades).
    HINT: You can use the builtin function sum() to get the sum of all items in a list.'''
    highest = 0
    student = ""

    for s in students:
        avg = sum(students[s])/len(students[s])
        if (avg > highest):
            highest = avg
            student = s

    return student

def main():

##    #testing for in_list
##    print(in_list([0, 4, 9, 11, 3, 0, 6], 0)) #should print True
##    print(in_list([7, 5, 10, 6, 4, 2], 12)) #should print False
##    print(in_list([], 1)) #should print False
##    print(in_list([4, 1, 8, 3, 9, 14, 15, 6, 5], 5)) #should print True

##    #testing for most_occurances
##    print(most_occurances([0, 7, 7, 1, 9, 4, 7, 3])) #should print 7
##    print(most_occurances(["cat", "dog", "bird", "cat", "snake", "fish"])) #should print cat
##    print(most_occurances([11])) #should print 11
##    print(most_occurances([13, "python", 13, "python", 13])) #should print 13

    #testing for highest_average
    dict1 = {"Sam": [82, 87, 91],
             "Lauren": [95, 90, 91],
             "Beth": [96, 87, 97],
             "James": [92, 88, 80],
             "Karen": [86, 90, 99]}
    print(highest_average(dict1)) #should print Beth

    dict2 = {"Jari": [94, 88, 89, 92],
             "Mayisha": [97, 96, 89, 92],
             "Flora": [91, 100, 85, 89],
             "Xin": [86, 89, 99, 93],
             "Cat": [88, 90, 94, 90],
             "Jocelyne": [90, 88, 87, 94],
             "Rachel": [83, 93, 91, 88],
             "Sophia": [91, 82, 88, 98]}

    print(highest_average(dict2)) #should print Mayisha

if __name__ == "__main__":
    main()
