'''
543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0  # variable to store the diameter

        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            
            # calculate diameter at each node
            self.diameter = max(self.diameter, left_height + right_height)
            
            return max(left_height, right_height) + 1

        height(root)
        return self.diameter

# Example usage:
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

solution = Solution()
print(solution.diameterOfBinaryTree(root))

'''
In this example, the diameterOfBinaryTree function calculates the diameter of the binary tree by calling the height function recursively for each node in the tree. The height function calculates the height of each subtree and updates the diameter accordingly. The final result is stored in the self.diameter variable.


The time complexity of the provided algorithm is O(N), where N is the number of nodes in the binary tree. This is because the algorithm visits each node exactly once during the recursive traversal, and for each node, it performs constant time operations.

The space complexity is O(H), where H is the height of the binary tree. This is because the algorithm uses recursion, and the maximum depth of the recursion stack is equal to the height of the tree. In the worst case, for a skewed tree, the height H could be equal to the number of nodes N, resulting in a space complexity of O(N). However, for a balanced tree, the height is logarithmic in the number of nodes, leading to a space complexity of O(log N).
'''