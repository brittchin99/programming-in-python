#SECTION 2: Function Practice
#INSTRUCTIONS - write code to finish each function below, then uncomment the tests to check your work

def multiply(num1, num2):
    '''takes two numbers and returns them multiplied'''

    return num1 * num2

def count_vowels(string):
    '''takes a string and returns the number of vowels in it'''
    count = 0
    vowels = "aeiouAEIOU"

    for letter in string:
        if letter in vowels:
            count+=1
    
    return count

def reverse(string):
    '''takes a string and returns it reversed'''
    reverse_string = ""

    for letter in string:
        reverse_string = letter + reverse_string
   
    return reverse_string

def main():

    #testing for multiply
##    print("TESTING MULTIPLY")
##    print(multiply(2, 3)) #should print 6
##    print(multiply(4, 4)) #should print 16
##    print(multiply(0, 30)) #should print 0
##    print(multiply(7, 1)) #should print 7

##    #testing for count_vowels
##    print("TESTING COUNT_VOWELS")
##    print(count_vowels("banana")) #should print 3
##    print(count_vowels("aaaeeeooo")) #should print 9
##    print(count_vowels("how many vowels in this sentence?")) #should print 9
##    print(count_vowels("@#$&!!")) #should print 0
##
    #testing for reverse
    print("TESTING REVERSE")
    print(reverse("dog")) #should print god
    print(reverse("python")) #should print nohtyp
    print(reverse("reverse this sentence")) #should print ecnetnes siht esrever
    print(reverse("racecar")) #should print racecar

if __name__ == "__main__":
    main()
