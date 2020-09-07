#PROJECT: Message Encryptor
#INSTRUCTIONS - create a message encryptor program
import random
from string import ascii_letters

#list of letter - numeric value pairs
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M" ,"N",
           "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def encrypt():
    '''encrypts a file with the given key'''
    print("ENCRYPT MESSAGE")
    key = input("What is the key you’d like to use?: ")
    file = input("What is the name of the file to be encrypted?: ")
    
    new_file = open(file, 'r') #opens the file the user inputted
    new_filename = "encoded_" + file.split(".")[0] + ".txt" #new filename
    coded_file = open(new_filename, 'w') #creates new file for data

    length = len(new_file.read()) #get the length of the document
    times = (length // len(key)) * key #multiply the key to match the number of characters in the doc

    new_file.seek(0) #go back to the top of the document
    i = 0

    #write encryption code here
    for line in new_file:
        for char in line:
            if char in ascii_letters: #if the character is a letter
                file_num = letters.index(char) #get numeric value of letter in file
                key_num = letters.index(times[i]) #get numeric value of letter in key
                letter_num = (file_num + key_num) % 26
                letter = letters[letter_num] #find the letter that corresponds to the new num
                i += 1
                coded_file.write(letter) #write letter to the coded file
            else:
                coded_file.write(char)
                
        coded_file.write('\n') #add newline char
                
    print("Encoded text has been written to {}.".format(new_filename))

    #close the files
    new_file.close()
    coded_file.close()

def decrypt():
    '''decrypts a file with the given key'''
    print("DECRYPT MESSAGE")
    key = input("What is the key you’d like to use?: ")
    file = input("What is the name of the file to be decrypted?: ")
    
    new_file = open(file, 'r') #opens the file the user inputted
    new_filename = "decoded_" + file.split(".")[0].split("_")[1] + ".txt" #new filename
    coded_file = open(new_filename, 'w') #creates new file for data

    length = len(new_file.read()) #get the length of the document
    times = (length // len(key)) * key #multiples the key to match the number of characters

    new_file.seek(0) #go back to the top of the document
    i = 0

    #write decryption code here
    for line in new_file:
        for char in line:
            if char in ascii_letters: #if the character is a letter
                file_num = letters.index(char) #get numeric value of letter in file
                key_num = letters.index(times[i]) #get numeric value of letter in key
                letter_num = (file_num - key_num) % 26
                letter = letters[letter_num] #find the letter that corresponds to the new num
                i += 1
                coded_file.write(letter) #write letter to the coded file
            else:
                coded_file.write(char)
                
        coded_file.write('\n') #add newline char
        
    print("Decoded text has been written to {}.".format(new_filename))

    #close the files
    new_file.close()
    coded_file.close()

def print_menu():
    '''prints the menu for the encryptor'''
    print("Welcome to the message encryptor.")
    print("MENU")
    print("1. Encrypt message")
    print("2. Decrypt message")

def main():
    print_menu()    

    action = input("What would you like to do? Please enter the option number: ")
    print()
    
    if (action == "1"):
        encrypt()
    else:
        decrypt()

if __name__ == "__main__":
    main()
