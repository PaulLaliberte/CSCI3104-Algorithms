#LastName:
#FirstName:
#Email:
#Comments:

from __future__ import print_function
import sys
import copy
import collections

# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields 
  
    def __init__(self, isRootNode):
        #The initialization below is just a suggestion.
        #Change it as you will.
        # But do not change the signature of the constructor.
        self.isRoot = isRootNode
        self.count = 0 # frequency count
        self.next = {} # Dictionary mappng each character from a-z to the child node


    def addWord(self,w):
        if len(w) != 0:
            if w[0] not in self.next:
                self.next[w[0]] = MyTrieNode(False)
                self = self.next[w[0]]
                self.addWord(w[1:])
            else:
                self = self.next[w[0]]
                self.addWord(w[1:])
        else:
            self.count += 1


        

    def lookupWord(self, w):
        if len(w) != 0:
            if w[0] not in self.next:
                return 0
            else:
                self = self.next[w[0]]
                return self.lookupWord(w[1:])
        else:
            return self.count




    def autoComplete(self,w):
        #Returns possible list of autocompletions of the word w
        #Returns a list of pairs (s,j) denoting that
        #         word s occurs with frequency j

        #YOUR CODE HERE
        
        return [('Walter',1),('Mitty',2),('Went',3),('To',4),('Greenland',2)] #TODO: change this line, please
    
    
            
"""
if (__name__ == '__main__'):
    t= MyTrieNode(True)
    lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']

    for w in lst1:
        t.addWord(w)

    j = t.lookupWord('testy') # should return 0
    j2 = t.lookupWord('telltale') # should return 0
    j3 = t.lookupWord ('testing') # should return 2
    print(j, j2, j3)
    #lst3 = t.autoComplete('pi')
    #print('Completions for \"pi\" are : ')
    #print(lst3)
    
    #lst4 = t.autoComplete('tes')
    #print('Completions for \"tes\" are : ')
    #print(lst4)
"""


 
    
    
     
