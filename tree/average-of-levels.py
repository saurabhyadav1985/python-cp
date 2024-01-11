'''
637. Average of Levels in Binary Tree

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
'''

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfLevels(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_sum = 0

        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        level_average = level_sum / level_size
        result.append(level_average)

    return result

# Example usage:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

output = averageOfLevels(root)
print(output)

'''
To solve the problem of finding the average values of nodes on each level in a binary tree, you can use a breadth-first search (BFS) approach. Here's a Python solution using a queue to traverse the tree level by level and calculate the average for each level:

The time complexity of the algorithm is O(N), where N is the number of nodes in the binary tree. This is because each node is visited once, and the inner loop processes all nodes at each level.

The space complexity is O(M), where M is the maximum number of nodes at any level in the binary tree. In the worst case, the queue can store all nodes at the maximum level. In a balanced binary tree, the maximum number of nodes at any level is approximately N/2, leading to O(N) space complexity.

Overall, the algorithm is efficient and scales linearly with the number of nodes in the tree.

Tip: maintain level_size ie queue size to pop exact number of items from queue on each level
'''