#read words from a file
#choose only words of a certain length
    #filter a list by string size
#get random entry from a list - random module. 
#print a word and guesses like B _ _ B A _ D
    #update the word afer each guess
    #change the values of the _ and shown letters
#get letter from user
    #casefold() the letter.
    #make sure it is only one character

import random
import string

def normalize_text(text):
        """Given a text, lowercases it, removes all punct, and removes white space. 
        double space will become single space"""
        #will convert any weird letters to standard case english
        text = text.casefold()
        #this will state that all upper and lower case letters are valid
        valid_chars = string.ascii_letters + string.whitespace + string.digits        
        #remove all punctuation
        new_text = ""
        for char in text:
            if char in valid_chars:
                new_text += char

        text = new_text
        text = text.replace("\n", " ")
        text = remove_small_words(text)
        return text

def remove_small_words(text):
    """Given a text, it will remove all words from the list that have fewer than 4 characters"""
    #creates a list
    words = []
    for word in text.split(" "):
        #checks to see if a word actually is there and if the length of the word is less than 4 characters
        if word != '' and len(word) >= 4:
            words.append(word) 
    return words

def random_word(text, difficulty):
    #creates a list of 4+ character words
    alist = normalize_text(text)
    new_list = []
    #takes the difficulty and creates a new list of words between 4 and 6 characters
    if difficulty == "easy":
        for word in alist:
            if word != '' and len(word) >= 4 and len(word) <= 6:
                new_list.append(word)
    #takes the difficulty and creates a new list of words between 6 and 8 characters
    if difficulty == "normal":
        for word in alist:
            if word != '' and len(word) >= 6 and len(word) <= 8:
                new_list.append(word)
    #takes the difficulty and creates a new list of words of 8 or more characters
    if difficulty == "hard":
        for word in alist:
            if word != '' and len(word) >= 8:
                new_list.append(word)     

    return new_list           

difficulty = input("What difficulty do you want to try (easy, normal, hard): ")
with open("words.txt") as file:
    text = file.read()
    your_word = random_word(text, difficulty)
    #will print out a randomized word from the current list based off the difficulty input
    print (random.choice(your_word))