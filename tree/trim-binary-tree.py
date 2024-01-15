'''
669. Trim a Binary Search Tree
Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

Example 1:

Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]
'''

class Solution:
    def trimBST(self, root, low, high):
        if not root:
            return None
        
        # If the current node value is outside the [low, high] range,
        # trim the subtree and move to the appropriate side
        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        
        # Recursively trim the left and right subtrees
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        return root
    
'''
Approach:

The given problem requires trimming a binary search tree such that all its elements lie within the range [low, high].
We can recursively traverse the tree and trim it based on the values at each node.
If the value is less than low, we can discard the entire left subtree, so we recursively trim the right subtree.
If the value is greater than high, we can discard the entire right subtree, so we recursively trim the left subtree.
If the value is within the range, we continue traversing and recursively trim both left and right subtrees.
Finally, we return the modified root.

Complexity Analysis:

The time complexity of the solution is O(n), where n is the number of nodes in the binary search tree. We potentially need to visit every node.
The space complexity is O(h), where h is the height of the tree. This is due to the recursive calls on the stack. In the worst case, for a skewed tree, the space complexity becomes O(n), but for a balanced tree, it is typically O(log n).
This solution trims the given binary search tree while maintaining the relative structure of all nodes within the specified range.
'''