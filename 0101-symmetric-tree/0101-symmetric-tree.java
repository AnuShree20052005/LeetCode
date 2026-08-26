class Solution {
    public boolean isSymmetric(TreeNode root) {
        return checkMirror(root.left, root.right);
    }

    private boolean checkMirror(TreeNode left, TreeNode right) {

        // Both are empty
        if (left == null && right == null) {
            return true;
        }

        // One is empty
        if (left == null || right == null) {
            return false;
        }

        // Values must be equal
        if (left.val != right.val) {
            return false;
        }

        // Check opposite sides
        return checkMirror(left.left, right.right)
            && checkMirror(left.right, right.left);
    }
}