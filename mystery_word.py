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
    """Given a text and a difficulty choice, this will go through and select words from the list that fall into the range of characters"""
    #calls normal_text which will creates a list of normal character and also remove words smaller than 4 characters
    alist = normalize_text(text)
    #creates a new list
    new_list = []
    #takes the difficulty and creates a new list of words between 4 and 6 characters
    if difficulty == "easy":        
        new_list = [word for word in alist if word != '' and len(word) >= 4 and len(word) <= 6]        
        # for word in alist:
        #     if word != '' and len(word) >= 4 and len(word) <= 6:
                # new_list.append(word)
    #takes the difficulty and creates a new list of words between 6 and 8 characters
    if difficulty == "normal":
        new_list = [word for word in alist if word != '' and len(word) >= 6 and len(word) <= 8]
  #takes the difficulty and creates a new list of words of 8 or more characters
    if difficulty == "hard":
        new_list = [word for word in alist if word != '' and len(word) >= 8]           
    return new_list           

def hide_word(word):
    """Given a word it will create a new dictionary of that word's key (the index of each letter), and value (either a '_ ' or '<the letter>')"""
    hidden_word = {}
    idx = 0
    for letter in word:
        hidden_word[idx] = '_'
        idx += 1
    return hidden_word

def update_hidden_word(hidden_word, your_word, guess):
    """Given a guess and the hidden_word will check to see if any letter match and replace the value of the '_ ' with the letter"""
    idx = 0    
    # hidden_word = [letter for letter in your_word if guess == letter and hidden_word[idx] == '_']
    for letter in your_word:
        if guess == letter and hidden_word[idx] == '_':
            hidden_word[idx] = letter
        idx += 1
    return hidden_word

def display_hidden_word(hidden_word):
    """Given a dict will transform into a displayable string"""
    display_word = ''
    for letter in hidden_word:
        display_word += hidden_word[letter]
    return display_word

def did_you_guess_it(word, guess, guesses):
    """Will decide if you guessed correctly and return a true/false"""
    for letter in word:
        if letter == guess and guess not in guesses:
            print ("You guessed a letter")
            return True
        if letter == guess and guess in guesses:
            print ("You already guessed that letter")
            return False
        if letter != guess and guess in guesses:
            return False           
        if letter != guess:
            continue
    return True

def remaining_guesses (word, guess, guesses):
    """Will decide if you guessed correctly and a true/false value"""
    guess_tracker = True
    for letter in word:
        if letter == guess and guess not in guesses:
            guess_tracker = True
            break
        if letter == guess and guess in guesses:
            guess_tracker = True
            break
        if letter != guess and guess in guesses:
            guess_tracker = True
            break    
        if letter != guess: 
            guess_tracker = False
            continue
    return guess_tracker

def continue_play ():
    """When the game is over the user will respond if they want to play again. Returns true or false"""
    play_again = input ("Do you want to play again? (y/n or yes/no)").lower()
    if play_again.isalpha() and play_again == "y" or play_again == "yes":
        print ("Very well, let's go...")
        return True
    if play_again.isalpha() and play_again == "n" or play_again == "no":
        print ("See you next time.")
        return False 


game_again = True
#while this is true the player will keep playing. If they input no when asked, it will end the loop
while game_again:
    game_on = True
    #while this is true the game will loop through and allow the player to keep guessing
    while game_on:
        difficulty = input("What difficulty do you want to try (easy, normal, hard): ").lower()
        #if the difficulty input matches the proper ask, it will go through the function
        if difficulty.isalpha() and difficulty == 'easy' or difficulty == 'normal' or difficulty == 'hard':
            with open("words.txt") as file:
                #sets the text file above as a long string
                text = file.read()
                #will take the long string and separate into a list, and the create a smaller list based on difficulty
                your_word = difficulty_list(text, difficulty)
                #will take your list and selects a random word.
                your_word = random.choice(your_word)
                #will replace your word with a dict that is filled with '_ '
                hidden_word = hide_word(your_word)
                #will turn your hidden_word dict and turn into a normal string
                display_word = display_hidden_word(hidden_word)
                print ("This is your word "+" ".join(display_word))
                guesses_left = 8
                guesses = []
                updated_word = {}
                #loop that checks over the amount of guesses remaining as well as if the word is completed
                #Chinh hovered over me to figure out which words items I needed to compare and how to fix a function.
                while guesses_left != 0 and your_word != display_word:
                    print (f"So far you've guessed: {guesses}")
                    guess = input ("Guess a letter in the mystery word: ").lower()
                    if guess.isalpha() and len(guess) == 1:
                        # calls function remaining_guesses to see if your guess was wrong. 
                        check = remaining_guesses(your_word, guess, guesses)
                        if check == False:
                            guesses_left -= 1
                            print ("You guessed incorreclty")
                        if did_you_guess_it(your_word, guess, guesses) == True:
                            guesses.append(guess)
                        print (f"You have {guesses_left} guesses remaining.")
                        #this will take the guess input and the random word and see if the letter is available. It will update the dict.
                        updated_word = update_hidden_word(hidden_word, your_word, guess)
                        display_word = display_hidden_word(updated_word)
                        print (" ".join(display_word))
                    else:
                        print ("Please try again. This time only enter one letter.")
            game_on = False
        else:
            print ("Please re-enter the difficulty.")
    if guesses_left != 0 and your_word == display_word:        
        print ("You got it! Great job!")           
        game_again = continue_play()
    if guesses_left == 0:
        print ("You lose! You get nothing!")
        print (f"Your word was {your_word.upper()}")
        game_again = continue_play()

