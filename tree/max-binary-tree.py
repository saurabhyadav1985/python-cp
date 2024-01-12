'''
654. Maximum Binary Tree

You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the subarray prefix to the left of the maximum value.
Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructMaximumBinaryTree(nums):
    if not nums:  # handle the empty array case
        return None

    max_val = max(nums)
    max_index = nums.index(max_val)

    root = TreeNode(max_val)
    root.left = constructMaximumBinaryTree(nums[:max_index])  # recursively build left subtree
    root.right = constructMaximumBinaryTree(nums[max_index+1:])  # recursively build right subtree

    return root

'''
Time Complexity: The time complexity of the algorithm is O(n^2) in the worst case. This occurs when the input array is sorted in ascending or descending order, as finding the maximum in each recursive call takes linear time, and there can be up to n recursive calls. However, on average, the algorithm has a time complexity of O(n log n), as the maximum value is not necessarily at the middle index.

Space Complexity: The space complexity of the algorithm is O(n) in the worst case. This occurs when the binary tree is skewed and takes up the entire space of the input array. In the average case, the space complexity is O(log n) due to the recursive calls.

Approach Explanation: The approach is based on recursively constructing the maximum binary tree. We find the maximum value in the input array and create a node with that value as the root. We then recursively build the left and right subtrees by passing the subarrays to the left and right of the maximum value. We repeat this process until the input array is empty or has only one element. The maximum binary tree is returned when the recursive calls reach the base case.
'''