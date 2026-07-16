# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):

        index = {}

        for i, val in enumerate(inorder):
            index[val] = i

        self.preIndex = 0

        def build(left, right):

            if left > right:
                return None

            rootVal = preorder[self.preIndex]
            self.preIndex += 1

            root = TreeNode(rootVal)

            mid = index[rootVal]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)