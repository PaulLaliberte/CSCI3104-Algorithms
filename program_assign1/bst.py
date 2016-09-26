"""Name: Paul Laliberte'
   On my honor as a University of Colorado Student, this code was entirely written by myself with no unauthorized help.

   Binary Search Tree
   Version: 3.x.x
"""

class Node:

    def __init__(self, my_key):
        self.key = my_key
        self.left = None
        self.right = None

    def insert(self, key_to_insert, node=None, nodeBool=False):
        if key_to_insert is self.key:
            pass
        elif key_to_insert < self.key and self.left is None:
            self.left = Node(key_to_insert)
        elif key_to_insert > self.key and self.right is None:
            self.right = Node(key_to_insert)
        elif key_to_insert < self.key and self.left is not None:
            if nodeBool is False:
                node = self.left
                self.insert(key_to_insert, node, True)
        elif key_to_insert > self.key and self.right is not None:
            if nodeBool is False:
                node = self.right
                self.insert(key_to_insert, node, True)


        if nodeBool is True:
            if key_to_insert is node.key:
                pass
            elif key_to_insert < node.key:
                if node.left is None:
                    node.left = Node(key_to_insert)
                else:
                    node = node.left
                    self.insert(key_to_insert, node, True)
            elif key_to_insert > node.key:
                if node.right is None:
                    node.right = Node(key_to_insert)
                else:
                    node = node.right
                    self.insert(key_to_insert, node, True)
            



    def inorder_traversal(self, ret_list):
        #return list of nodes of inorder

        pass

    def get_depth(self):
        #return depth
        pass

    def key_exists(self, key, node=None):
        
        key_found = False

        if key is self.key:
            key_found = True
            return key_found

        elif node is None:
            if self.left is None and self.right is None:
                return False
            elif key < self.key and self.left is not None:
                node = self.left
                return self.key_exists(key, node)
            elif key > self.key and self.right is not None:
                node = self.right
                return self.key_exists(key, node)
            else:
                return False

        elif node is not None:
            if key is node.key:
                key_found = True
                return key_found
            elif key < node.key and node.left is not None:
                node = node.left
                return self.key_exists(key, node)
            elif key > node.key and node.right is not None:
                node = node.right
                return self.key_exists(key, node)
            else:
                return key_found



"""
if __name__ == '__main__':
    print('Please do not call this file directly.')
    print('To run autograder script: please call the test_bst.py')
"""


