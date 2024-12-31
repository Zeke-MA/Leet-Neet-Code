from typing import Optional

'''
https://neetcode.io/problems/depth-of-binary-tree

Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:



Input: root = [1,2,3,null,null,4]

Output: 3
Example 2:

Input: root = []

Output: 0
Constraints:

0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100

'''


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        leftDep = self.maxDepth(root.left)
        rightDep = self.maxDepth(root.right)

        return max(leftDep, rightDep) + 1
    
solution = Solution()

print(solution.maxDepth([1,2,3,None,None,4]))
print(solution.maxDepth([]))