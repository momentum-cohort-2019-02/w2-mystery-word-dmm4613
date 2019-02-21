#read words from a file (check)
#choose only words of a certain length (check)
    #filter a list by string size (check)
#get random entry from a list - random module. (check)
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
        #this function removes all words smaller than 4 letters
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

def difficulty_list(text, difficulty):
    #calls normal_text which will creates a list of normal character and also remove words smaller than 4 characters
    alist = normalize_text(text)
    #creates a new list
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

def hide_word(word):
    """Given a word it will create a new dictionary of that word's key (the index of each letter), and value (either a '_ ' or '<the letter>')"""
    hidden_word = {}
    idx = 0
    for letter in word:
        hidden_word[idx] = '_ '
        idx += 1
    return hidden_word

def update_hidden_word(word, guess):
    """Given a guess and the hidden_word will check to see if any letter match and replace the value of the '_ ' with the letter"""
    hidden_word = {}
    idx = 0    
    for letter in word:
        if guess != letter:
            hidden_word[idx] = '_ '
            idx += 1
        else:
            hidden_word[idx] = letter+' '
            idx += 1
    return hidden_word

def display_hidden_word(hidden_word):
    """Given a dict will transform into a displayable string"""
    display_word = ''
    for letter in hidden_word:
        display_word += hidden_word[letter]
    return display_word


difficulty = input("What difficulty do you want to try (easy, normal, hard): ")
with open("words.txt") as file:
    #sets the text file above as a long string
    text = file.read()
    #will take the long string and separate into a list, and the create a smaller list based on difficulty
    your_word = difficulty_list(text, difficulty)
    #will take your list and selects a random word.
    your_word = random.choice(your_word)
    print (your_word)
    #will replace your word with a dict that is filled with '_ '
    hidden_word = hide_word(your_word)
    print (f"{hidden_word}")
    #will turn your hidden_word dict and turn into a normal string
    display_word = display_hidden_word(hidden_word)
    print (display_word)
    guesses_left = 8
    while guesses_left != 0:
        guess = input ("Guess a letter in the mystery word: ")
        #this will take the guess input and the random word and see if the letter is available. It will update the dict.
        updated_word = update_hidden_word(your_word, guess)
        print (updated_word)
        display_word = display_hidden_word(updated_word)
        print (display_word)

