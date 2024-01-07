'''
108. Convert Sorted Array to Binary Search Tree
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums:
        return None
    
    mid = len(nums) // 2
    
    # Create a new node with the middle element as the root
    root = TreeNode(nums[mid])
    
    # Recursively build the left and right subtrees
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    
    return root

# Example usage:
nums = [-10, -3, 0, 5, 9]
result_tree = sortedArrayToBST(nums)

'''
In this code, the sortedArrayToBST function takes a sorted array nums as input and recursively builds a height-balanced binary search tree. The middle element of the array is chosen as the root of the current subtree, and then the function is called recursively on the left and right halves of the array to build the left and right subtrees, respectively. The process continues until the entire tree is constructed.

You can adjust the nums array according to your input and use the result_tree as the root of the resulting binary search tree.


The time complexity of the provided algorithm for converting a sorted array to a binary search tree is O(n), where n is the number of elements in the array.

Explanation:

At each level of the recursion, the algorithm processes each element in the array once.
The division of the array into halves and the creation of nodes occur in constant time for each element.
Since each element in the array is processed once, and the array is divided into halves recursively, the overall time complexity is O(n), where n is the number of elements in the array.
The space complexity is also O(n) due to the recursive call stack, where the maximum depth of the recursion is proportional to the height of the resulting binary search tree, which is log(n) for a balanced tree.
'''