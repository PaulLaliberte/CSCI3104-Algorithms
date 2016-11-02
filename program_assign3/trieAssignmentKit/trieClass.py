#LastName:
#FirstName:
#Email:
#Comments:

from __future__ import print_function
import sys
import copy

# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields 
  
    def __init__(self, isRootNode):
        #The initialization below is just a suggestion.
        #Change it as you will.
        # But do not change the signature of the constructor.
        self.isRoot = isRootNode
        self.isWordEnd = False # is this node a word ending node
        #self.isRoot = False # is this a root node
        self.count = 0 # frequency count
        self.next = {} # Dictionary mappng each character from a-z to the child node


    def addWord(self,w):
        if len(w) != 0:
            for i in range(0, len(w)):
                if w[i] not in self.next:
                    array = []
                    try:
                        tup = (w[i+1], MyTrieNode(False))
                        array.append(tup)
                        self.next[w[i]] = array
                    except IndexError:
                        #end of word
                        pass
                else:
                    try:
                        inArray = False
                        tmp = self.next[w[i]]
                        for j in tmp:
                            if w[i+1] in j:
                                inArray = True

                        if inArray is False:
                            tup = (w[i+1], MyTrieNode(False))
                            array = self.next[w[i]]
                            newArray = copy.copy(array)
                            print(newArray)
                            newArray.append(tup)
                            self.next[w[i]] = newArray
                    except IndexError:
                        #end of word
                        pass


        

    def lookupWord(self,w):
        # Return frequency of occurrence of the word w in the trie
        # returns a number for the frequency and 0 if the word w does not occur.

        # YOUR CODE HERE
        
        return 0 # TODO: change this line, please
    

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
    lst3 = t.autoComplete('pi')
    print('Completions for \"pi\" are : ')
    print(lst3)
    
    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)
"""

 
    
    
     
