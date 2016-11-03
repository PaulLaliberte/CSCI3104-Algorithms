#LastName: Laliberte'
#FirstName: Paul
#Email: pala5552@colorado.edu
#Comments: DFS implemented

from __future__ import print_function
import sys
import copy

class MyTrieNode:
  
    def __init__(self, isRootNode):
        self.isRoot = isRootNode
        self.count = 0 
        self.next = {} 


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


    def depthFirstSearch(self, char, array):
        if self.count > 0:
            array.append((char, self.count))

        if len(self.next.keys()) == 0:
            return

        for k in self.next.keys():
            self.next[k].depthFirstSearch(char+k, array)


    def autoComplete(self, w, array=[], char=''):
        if len(array) > 0:
            array = []

        if len(w) != 0:
            if w[0] not in self.next:
                array = []
                return array
            else:
                self = self.next[w[0]]
                char += w[0]
                return self.autoComplete(w[1:], array, char)
        
        else:
            if self.count > 0:
                array.append((char, self.count))

            for k in self.next.keys():
                self.next[k].depthFirstSearch(char+k, array)

            return array

      

if (__name__ == '__main__'):
    t= MyTrieNode(True)
    lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']

    for w in lst1:
        t.addWord(w)

    j = t.lookupWord('testy') # should return 0
    j2 = t.lookupWord('telltale') # should return 0
    j3 = t.lookupWord ('testing') # should return 2
    print(j, j2, j3)
    lst3 = t.autoComplete('pi')
    print('Completions for \"pi\" are : ')
    print(lst3)
    
    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)




 
    
    
     
