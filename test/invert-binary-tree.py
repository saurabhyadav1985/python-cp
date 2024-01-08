'''
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
'''
class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = None
        self.right = None
        
    def invertTree(self, root):
        if not root:
            return None
        
        output = TreeNode(root.val)
        
        if root.left:
            output.right = invertTree(root.left)
        if root.right:
            output.left = invertTree(root.right)
        
        return output
        
        
    def traverse(self, root):
        if not root:
            return
    
        queue = [root]
        while queue:
            current_level_size = len(queue)
            for i in range(current_level_size):
                node = queue.pop(0)
                print(node.value, end = " ")
                if not root.left:
                    queue.append(root.left)
                if not root.right:
                    queue.append(root.right)
        
            print()
            
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    inverted_tree = invertTree()
    print(traverse(inverted_tree))