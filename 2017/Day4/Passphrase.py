from inspect import _void
from tkinter import W


class Passphrase:

    def __init__(self,filename):
        with open(filename, 'r') as input_file:    
            self.phrase_list = [line.strip('\n').split(' ') for line in input_file]

    def valid_phrases(self) -> int:
        valid_phrase_count = 0
        for phrase in self.phrase_list:
            word_count = dict()
            for word in phrase:
                try: 
                    word_count[word] += 1
                    break
                except KeyError:
                    word_count[word] = 1
            else:
                valid_phrase_count += 1
        return valid_phrase_count    

    def valid_phrases2(self) -> int:
        valid_phrase_count = 0
        for phrase in self.phrase_list:
            anagram = dict()
            for word in phrase:
                sorted_word = ''.join(sorted(word))
                if sorted_word in anagram.keys():
                    break
                else:
                    anagram[sorted_word] = 1
            else:
                valid_phrase_count += 1
        return valid_phrase_count
        