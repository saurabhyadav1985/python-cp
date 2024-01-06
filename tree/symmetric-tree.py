#101. Symmetric Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    if not root:
        return True
    
    def isMirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)
    
    return isMirror(root.left, root.right)

# Example usage:
# Construct a symmetric tree
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(2, TreeNode(4), TreeNode(3))

'''
To check whether a binary tree is symmetric (i.e., a mirror of itself), you can use a recursive approach to compare the left and right subtrees. Here's a Python implementation

This code defines a TreeNode class representing a node in the binary tree. The isSymmetric function checks if the given tree is symmetric by calling the recursive helper function isMirror, which compares the left and right subtrees of the current node. If both subtrees are mirrors of each other, the tree is symmetric.

The time complexity of the above algorithm is O(n), where n is the number of nodes in the binary tree. This is because each node is visited once, and the comparison and recursive calls are constant time operations.

The space complexity is O(h), where h is the height of the binary tree. In the worst case, the recursive calls can go as deep as the height of the tree. In a balanced binary tree, the height is O(log n), but in the worst case (for example, a skewed tree), the height can be O(n). Therefore, in the worst case, the space complexity is O(n).
'''