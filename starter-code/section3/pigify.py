#starter code for Pyg Latin exercise

def splitSentence(sentence):
    '''takes a String sentence and returns a List corresponding to the sentence split by spaces'''
    return sentence.split()

def indexOfFirstVowel(word):
    '''takes a String word and returns the index of the first vowel - returns null if no vowel found'''
    index = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for i in range(len(word)):
        if (word[i] in vowels):
            return i
    return null
    

def pigify(sentence):
    '''takes a String sentence from the user and returns the sentence pigified.'''
    #create a string for the pigified sentence
    pigified = ""
    
    #split the sentence into individual words
    words = splitSentence(sentence)
    
    #for each word, check if the length > 3
    for word in words:
        if (len(word) > 3):
            #find the index of first vowel
            index = indexOfFirstVowel(word)

            #slice the string before the first vowel
            front = word[0:index]

            #update the word to remove the front
            word = word[index:]

            #append the front to the end of the word and add 'ay'
            word = word + front + "ay"

        #else, add word to the pigified string
        pigified = pigified + word + ' '

    return pigified.strip()

def main():
    sentence = input("Enter a sentence: ")
    print(pigify(sentence))

if __name__ == "__main__":
    main()
