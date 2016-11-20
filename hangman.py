import random
obrazky = [
"""~~~~~~~""",
"""+
|
|
|
|
|
~~~~~~~""",
"""
+---.
|
|
|
|
|
~~~~~~~ """,
"""
+---.
|   |
|
|
|
|
~~~~~~~""",
"""
+---.
|   |
|   O
|
|
|
~~~~~~~""",
"""
+---.
|   |
|   O
|   |
|
|
~~~~~~~""",
"""
+---.
|   |
|   O
| --|
|
|
~~~~~~~""",
"""
+---.
|   |
|   O
| --|--
|
|
~~~~~~~""",
"""
+---.
|   |
|   O
| --|--
|  /
|
~~~~~~~""",
"""
+---.
|   |
|   O
| --|--
|  / \
|
~~~~~~~"""]


def find_all(letter,field):
    indices = [i for i, x in enumerate(field) if x == letter]
    return indices

# define a function for generating a random word
def choose_word():
    words = ['hackathon']
    return random.choice(words)

word = choose_word()

field = '-'*len(word)

score = 0

# main loop
while True:
    # print out current state of the game
    # for example - We're guessing the word: _ _ _ _ _ _ _ _ _ _
    print(field)

    # let's get a letter from the user
    while True:
        try:
            letter = str(input("Guess the letter: "))
        except ValueError:
            print('Choose letter')
    # make sure the letter is only one character
        if len(letter) == 1:
            break
        
    # print the letter to see if everything is ok by now
    print("You guessed", letter)
    print(field)

    # determine if the letter is in the word
    if letter not in word:
        score += 1
        print(obrazky[score])
        if score == len(obrazky):
            print('You loose!')
    else: 
        field = ''.split(field)
        for i in range(len(field)):
            if word[i] == letter:
                field[i] = letter
            else:
                pass
                
                
        field = ''.join(field)

        
       
       
       
       
#        for i in range(len(word)):
#            if word[i] == letter:
#                field = field[:i]+letter+field[i:]
#            else:
#                pass
#        field = [letter if i==letter else '-' for i in word]
#        field = ''.join(field)        
        

#        indices = find_all(letter,field)
#        for i in indices:
#            field[indices[i]] = letter
#            print(field)
    # check if the word is not guessed in its entirety
    
    
    
    
    
    
