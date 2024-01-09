"""Word Finder: finds random words from a dictionary."""

import random
class WordFinder:
    ...

    def __init__(self, path):
        """This tell the path to open to the file
           then tells the console to report how many items were read
        """
        dict_file = open(path)
        self.words = self.parse(dict_file)
        
        print(f"{len(self.words)} words read")
        
    def parse(Self, dict_file):
        """this gets a list of words in the file"""
        return  [w.strip() for w in dict_file]
        
    def random_word(self):
        """this then pulls a word out of the list"""
        
        return random.choice(self.words)
    
class SpecialWordsFinder(WordFinder):
    """this returns three words and makes sure there is no # in it"""
    def parse(Self, dict_file):
        """this tells the console to get a word out then checks to see if it starts with a # if it does then it moves on"""
        return [w.strip() for w in dict_file if w.strip and not w.startswith('#')]