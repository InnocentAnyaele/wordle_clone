""" 
A wordle game clone done with a python class.
See https://www.nytimes.com/games/wordle/index.html for how wordle is played. 
Color code - "g" (green), "b" (black) or "y" for yellow

"""


import random
from colorama import Fore, Back, Style

class Wordle:
    
    # our constructor class initiates a word list 
    def __init__(self):
        self.word_list = ["aback", "abase", "abate", "abbey", "abbot", "abhor", "abide", "abled", "abode", "abort", "about", "above" ] # list of words used in the game
        self.list_length = len(self.word_list) # length of list
      
    # random word function spits out a random word from our word list in our constructor 
    def random_word(self):
        self.random_number = random.randint(0,self.list_length - 1)
        return (self.word_list[self.random_number])
    
    
    """
    The play function is what is called to begin the game. It creates a dictionary of all the alphabets all with the value "b".
    The "b" value, stands for the black color code i.e "g" (green), "b" (black) or "y" for yellow. This will be important in the
    print function as the letters will be printed later with their corresponding colors. It then asks the user for an attempt, 
    and after validation, it creates an array of each letter of the attempt per their respective color code for each attempt and 
    stores all the arrays in the attemptsArray. 
    """
    def play(self): 
        self.attemptsArray = []
        random_word = self.random_word()
        print (random_word)
        self.word_dict = {}    
        alpha = 'abcdefghijklmnopqrstuvwxyz'       
        for w in alpha:
            self.word_dict[w] = 'b'
                    
        count = 5
        while count > 0:
            self.print_all() # prints all alphabets and their color codes 
            self.print_guesses() # print all the attempts done by the user
            print ('You have ' + str(count) + ' attempts left')        
            attempt = input("Please input a 5 letter word ----->")
            attempt.upper()
            if attempt not in self.word_list:
                print ("Word is not in list")
            if len(attempt) != 5:
                print ("Word must contain 5 letters")
            if not attempt.isalpha():
                print ("Word must contain only alphabets")
            if len(attempt) == 5 and attempt in self.word_list:
                currentArray = []
                for idx, a in enumerate(attempt):
                    # for r in random_word:
                        if a == random_word[idx]:
                            currentArray.append(a + '.g')
                            self.word_dict[a] = 'g'
                        elif a != random_word[idx] and a in random_word:
                            currentArray.append(a + '.y')
                            self.word_dict[a] = 'y'
                        else:
                            currentArray.append(a + '.b')
                            self.word_dict[a] = 'b'
                self.attemptsArray.append(currentArray)
                if attempt == random_word:
                    self.print_all()
                    self.print_guesses()
                    print ("You guessed correctly")
                    return
                count -= 1
        self.print_all()
        self.print_guesses()
        print ("You failed to guess correctly")
        print ("The word is " + random_word)
        return
        
    """
    our print_all class takes all the alphabets (key) in the word_dict and prints them with their corresponding colors (value) 
    using the colorama library
    Every entry in the dictionary contains an alphabet with a value of either "g" (green), "b" (black) or "y" for yellow. 
    The function then takes each key, checks the corresponding color code and prints it out.
     
    """
    def print_all(self):
        print ('\n')
        print ('-------------alphabets--------------')
        print ('\n')
        for w in self.word_dict:
            if self.word_dict[w] == 'b':
                print (Back.BLACK + w + Style.RESET_ALL, end=" ")
            elif self.word_dict[w] == 'g':
                print (Back.GREEN + w + Style.RESET_ALL, end=" ")
            elif self.word_dict[w] == 'y':
                print (Back.YELLOW + w + Style.RESET_ALL, end=" ")
        print ('\n')
        print ('--------------------------------------')
        
    
    """ 
    The print guesses class prints out each letter in each guess in our attempts array per their colour code.
    Our attempts array is an array of arrays with each array contain strings of two letters. e.g "a.g" The first letter 
    being the attempt of the user and the second the responding color code i.e "g" (green), "b" (black) or "y" for yellow.
    The function, checks for each of the arrays, and print the letters of each array per their color code.  
    """
        
    def print_guesses(self):
        for i in range(0,len(self.attemptsArray)):
            for j in range(0,len(self.attemptsArray[i])):
                split_word = self.attemptsArray[i][j].split('.')
                if split_word[1] == 'b':
                    print (Back.BLACK + split_word[0] + Style.RESET_ALL, end=" ")
                elif split_word[1] == 'g':
                    print (Back.GREEN + split_word[0] + Style.RESET_ALL, end =" ")
                elif split_word[1] == 'y':
                    print (Back.YELLOW + split_word[0] + Style.RESET_ALL, end = " ")
            print ('\n')
                
                    
                
wordle = Wordle()
wordle.play()