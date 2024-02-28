# Griffin Graham
# Class: CS120
# Assignment: PS05 - String Processing
# 11/08/2023

def pullUpper(inputString): #Method to pull out the uppercase letters to print out.
    identifiedLetters = []
    for index in inputString: #Iterate through each character in the string.
        if index.isupper(): #If true
            identifiedLetters.append(index) #Add the value of index to the arrary.
    finalString = ", ".join(identifiedLetters) #Create a string based on the values of the array.
    print("Uppercase Letters:", finalString) #Printing out the string.

def secondLetter(inputString): #Method to acquire only the second letter from every individual word.
    wordSplit = inputString.split(" ") #Splitting the string based on spaces to create individual entries for every word.
    identifiedLetters = [] #Initializing the array.
    for x in wordSplit: #Iterate through each word in the array.
        if len(x) > 1: #Using this to ensure that it is not a single letter like "a"
            identifiedLetters.append(x[1]) #Add the character at index 1 for each word to the array.
    finalString = ", ".join(identifiedLetters) #Create a string based on the values of the array.
    print("Every Second Letter:",finalString) #Printing out the string.

def underscoreReplace(inputString): #Method to identify vowels and replace with an underscore.
    vowels = ['a','e','i','o','u'] #Creating an array to check values against.
    finalString = ''
    for x in inputString: #Iterating through every character in the string.
        if x.lower() in vowels: #Checking to see if the value of the spot is within the vowels array.
            finalString += '_' #Rewriting the string's position with an underscore.
        else:
            finalString += x #If it's not a value, adds the original character to finalString.
    print("Replace Vowels:",finalString) #Printing out the string.

def numberOfVowels(inputString): #Method to count up the number of values.
    vowels = ['a','e','i','o','u'] #Creating an array to check values against.
    vowelCount = 0 #Count number for how many values exist in the string.
    for x in inputString: #Iterating through every character in the string.
        if x.lower() in vowels: #Checking to see if the value of the spot is within the vowels array.
            vowelCount += 1 #Incrementing the count if there's a vowel.
    print("Count Vowels:",vowelCount) #Printing out the value of vowelCount.

def vowelPositions(inputString): #Method to return the index numbers for any vowels in the string.
    vowels = ['a','e','i','o','u'] #Creating an array to check values against.
    vowelIndexes = [] #Initializing an array to keep track of index numbers.
    index = -1 #Starting index at -1 in order to count properly from 0 for the for loop.
    for x in inputString: #Iterating through every character in the string.
        index += 1 #Incrementing the index through.
        if x.lower() in vowels: #Checking to see if the value of the spot is within the vowels array.
            vowelIndexes.append(index) #Adding the index value into the array of indexes.
    print("Vowel Positions:",vowelIndexes) #Printing out the array.

def main(): #Using a main method to call the individual methods.
    userInput = input("Enter in a String for us to manipulate: ") #Taking input, then passing to all of the individual methods for the assignment requirements.
    pullUpper(userInput)
    secondLetter(userInput)
    underscoreReplace(userInput)
    numberOfVowels(userInput)
    vowelPositions(userInput)

if __name__ == "__main__":
    main()