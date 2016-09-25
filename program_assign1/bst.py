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
        if key_to_insert < self.key and self.left is None:
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
            if key_to_insert < node.key:
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

    def key_exists(self, key):
        if key is self.key:
            return True
        elif key < self.key:
            node = self.left
            findKey(node, key)
        else:
            node = self.right
            findKey(node, key)
            findKey(node, key)

    def findKey(self, node, key):
        if key is node.key:
            return True
        elif key < node.key:
            node = node.left
            findKey(node, key)
        else:
            node = node.right
            findKey(node, key)




"""
if __name__ == '__main__':
    print('Please do not call this file directly.')
    print('To run autograder script: please call the test_bst.py')
"""


"""
        if key_to_insert is self.key:
            pass
        elif key_to_insert < self.key:
            if self.left is None:
                self.left = Node(key_to_insert)
            else:
                curr = self.left
                while curr:
                    if key_to_insert is curr.key:
                        break
                    elif curr.left is None:
                        curr.left = Node(key_to_insert)
                        break
                    elif curr.right is None:
                        curr.right = Node(key_to_insert)
                        break
                    elif key_to_insert < curr.key and curr.left is not None:
                        curr = curr.left
                    else:
                        curr = curr.right

        else:
            if self.right is None:
                self.right = Node(key_to_insert)
            else:
                curr = self.right
                while curr:
                    if key_to_insert is curr.key:
                        break
                    elif curr.left is None:
                        curr.left = Node(key_to_insert)
                        break
                    elif curr.right is None:
                        curr.right = Node(key_to_insert)
                        break
                    elif key_to_insert < curr.key and curr.left is not None:        
                        curr = curr.left
                    else:
                        curr = curr.right  
        """


"""
        key_found = False

        if key is self.key:
            key_found = True
        elif key < self.key:
            curr = self.left
            while curr:
                if key is curr.key:
                    key_found = True
                    return key_found
                elif key < curr.key:
                    curr = curr.left
                else:
                    curr = curr.right

        else:
            curr = self.right
            while curr:
                if key is curr.key:
                    key_found = True
                    return key_found
                elif key < curr.key:
                        curr = curr.left
                else:
                        curr = curr.right
                
        return key_found
    """

