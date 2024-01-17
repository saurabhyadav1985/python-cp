# 589 "N-ary Tree Preorder Traversal":

class Solution:
    def preorder(self, root):
        result = []
        self.preorderTraversal(root, result)
        return result
    
    def preorderTraversal(self, node, result):
        if node is None:
            return
        
        result.append(node.val)  # Visit the current node
        
        for child in node.children:  # Traverse each child recursively
            self.preorderTraversal(child, result)

'''
Approach:

The problem requires performing a preorder traversal of an n-ary tree and returning the values of the nodes.
Preorder traversal visits the current node before its children. To implement this, we'll use a recursive approach.
We define a helper function preorderTraversal() that takes a node and a list result to store the values.
In the preorderTraversal() function, we first check if the current node is None. If so, we return.
Next, we append the value of the current node to the result list.
Then, we iterate over each child of the current node and recursively call preorderTraversal() for each child.
Finally, we have another function called preorder() that initializes an empty list result and calls preorderTraversal() with the root node and the result list. It then returns the result list.
Complexity Analysis:

The time complexity of this approach is O(n), where n is the total number of nodes in the n-ary tree. We need to visit every node once in the worst case.
The space complexity is O(n), as we use additional space to store the result list. In the worst case, the result list may contain all the nodes' values.

If using iterative approach you need to use Stack.
'''