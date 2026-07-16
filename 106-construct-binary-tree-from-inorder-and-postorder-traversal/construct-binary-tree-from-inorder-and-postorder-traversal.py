# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder, postorder):

        index = {}

        for i, val in enumerate(inorder):
            index[val] = i

        self.postIndex = len(postorder) - 1

        def build(left, right):

            if left > right:
                return None

            rootVal = postorder[self.postIndex]
            self.postIndex -= 1

            root = TreeNode(rootVal)

            mid = index[rootVal]

            # Build right first
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)