'''
538. Convert BST to Greater Tree

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:

Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root):
        self.sum = 0  # Initialize a variable to store the running sum

        def reverse_inorder_traversal(node):
            nonlocal self

            if node is not None:
                # Traverse the right subtree
                reverse_inorder_traversal(node.right)

                # Update the node value with the running sum
                self.sum += node.val
                node.val = self.sum

                # Traverse the left subtree
                reverse_inorder_traversal(node.left)

        # Start the traversal from the root
        reverse_inorder_traversal(root)

        return root
    
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)

solution = Solution()
new_root = solution.convertBST(root)

'''
This algorithm works by visiting nodes in a reverse in-order traversal, updating each node's value with the running sum of greater keys encountered so far.

The time complexity of the given algorithm is O(N), where N is the number of nodes in the Binary Search Tree (BST). This is because each node is visited exactly once during the reverse in-order traversal.

The space complexity is O(H), where H is the height of the BST. This is due to the recursive call stack during the traversal. In the worst case, when the BST is skewed (a degenerate tree), the height H approaches N, resulting in O(N) space complexity. However, in a balanced BST, the height is logarithmic, leading to a space complexity of O(log N).
'''